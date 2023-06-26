from pymongo import MongoClient
from dotenv import load_dotenv
import os

connection_string = os.getenv("AZURE_DB_CONNECTION_STRING")
client =  MongoClient(connection_string)
database = client["PHR"]
collection = database["PHR"]
user_collection = database["PHR_User"]