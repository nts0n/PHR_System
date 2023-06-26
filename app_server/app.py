from flask import Flask, request, jsonify
from flask_talisman import Talisman
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.core.engine.util import objectToBytes,bytesToObject
import hashlib
import pickle
import json
from io import BytesIO
#import ssl
from bson.objectid import ObjectId
from key_vault import *
from db_request import *
import base64


app = Flask(__name__)
talisman = Talisman(app)
val_info = None

# Initialize a pairing group
group = PairingGroup('MNT224')
cpabe = CPabe_BSW07(group)



@app.route('/', methods=['GET'])
def index():
    return "welcome"

# Define a function to generate keys for a user
# @app.route('/generate_user_key', methods=['POST'])
def generate_user_key(attributes):
    """
    Generates a key for a user with the given attributes.
    """
    str_master_key = secret_client.get_secret("master-key").value
    str_master_public_key = secret_client.get_secret("master-public-key").value


    # convert keys to bytes b''
    master_key = str_master_key[2:-1].encode()
    master_public_key = str_master_public_key[2:-1].encode()
    
    # convert keys to dict for encryption
    master_key = bytesToObject(master_key, group)
    master_public_key = bytesToObject(master_public_key, group)

    user_key = cpabe.keygen(master_public_key, master_key, attributes)

    user_key = objectToBytes(user_key, group)

    return user_key.decode()

@app.route('/get_key', methods=['POST'])
def key_get():
    str_master_public_key = secret_client.get_secret("master-public-key").value
    master_public_key = str_master_public_key[2:-1]
    return master_public_key


@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    collection.insert_one(data)
    return jsonify({'data':'success'})
    

@app.route('/download', methods=['POST'])
def download():
    filename = request.json['filename']
    data = collection.find_one({"_id":ObjectId(filename)})
    
    return_document = {
        'master_pk' : key_get(),
        'user_secret_key': generate_user_key(val_info["attribute"]),
        "ciphertext": data["ciphertext"],
        "key": data["key"]
    }
    return jsonify(return_document)
    


@app.route("/login",methods=["POST"])
def login():
    username = request.json['username']
    
    password = request.json['password'].strip()
    print(type(password))
    data = user_collection.find({"username":username})
    global val_info
    val_info = dict(data.next())
    if username == val_info["username"] and password == val_info["password"]:
        return jsonify({'attributes' : val_info['attribute']})
    return "false"

@app.route("/search", methods=["POST"])
def searching():
    id_search = request.json['patient_id']
    data = []
    documents = collection.find({"patient_id": id_search})
    for document in documents:
        
        data.append(str(document['_id']))
    
    return jsonify({'key_value':data})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
