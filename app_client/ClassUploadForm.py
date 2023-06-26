import tkinter as ctk
from tkinter import messagebox, filedialog
import json
import requests
# from Crypto.Cipher import AES, GCM
from Crypto.Random import get_random_bytes
from charm.core.engine.util import objectToBytes,bytesToObject
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64



class UploadForm(ctk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_ui(master)
        self.file_content = None

    def create_ui(self, master):
        import ClassContainer

        # create back button
        self.backBtn = ctk.Button(self, text="Back", font=("Arial",12),command=lambda: [master.show_frame(ClassContainer.MenuForm)])
        self.backBtn.place(x=20,y=20)

        # create logout button
        self.logoutBtn = ctk.Button(self, text="Logout", font=("Arial",12),command=lambda: [master.show_frame(ClassContainer.LoginForm)])
        self.logoutBtn.place(x=800,y=20)

        # create title label
        self.titleLabel = ctk.Label(self, text="Upload PHR Document", font=("Arial",26))
        self.titleLabel.pack(pady=(30,0))

        self.policyLabel = ctk.Label(self, text="Enter policy:",font=("Arial",22))
        self.policyLabel.pack(pady=(20,0))

        self.txtPolicy = ctk.Entry(self, font=("Arial",14),width=800)
        self.txtPolicy.pack(padx=100,pady=(20,20))

        # create content (document) view text box
        self.txtDocumentView = ctk.Text(self,font=("Arial",12),width=100, height=50)
        # self.txtDocumentView.place(x=150,y=150)
        self.txtDocumentView.pack(padx=50,pady=(20,100))

        # create select button
        self.selectBtn = ctk.Button(self, text="Select", font=("Arial",14), command=lambda: [self.select_event()])
        self.selectBtn.place(x=300,y=600)

        # create upload button
        self.uploadBtn = ctk.Button(self, text="Upload", font=("Arial",14), command=lambda: [self.upload_event()])
        self.uploadBtn.place(x=420,y=600)

    def select_event(self):
        try:
            file_path = filedialog.askopenfilename()
            with open(file_path, 'rb') as file:
                self.file_content = file.read()
            if self.file_content:
                self.txtDocumentView.delete(1.0, ctk.END)
                self.txtDocumentView.insert(ctk.END,self.file_content.decode())
        except:
            pass
    def aes_encrypt(self):

        aes_key = AESGCM.generate_key(bit_length=256)
        aes = AESGCM(key=aes_key)
        nonce = os.urandom(12)

        ciphertext = aes.encrypt(data=self.file_content,associated_data=None,nonce=nonce)
        return (ciphertext, aes_key, nonce)

    def cpabe_encrypt(self, aes_key, nonce):
        from ClassContainer import url
        
        group = PairingGroup('MNT224')
        cpabe = CPabe_BSW07(group)
        hyb_abe = HybridABEnc(cpabe, group)

        public_key = requests.post(url + 'get_key').content

        public_key = bytesToObject(public_key,group)

        access_policy = self.txtPolicy.get().strip()

        encrypted_aes_key = hyb_abe.encrypt(public_key, aes_key + b',' + nonce, access_policy)
        
        return encrypted_aes_key


    
    def upload_event(self):
        try:
            from ClassContainer import url
            group = PairingGroup('MNT224')


            url_up = url + 'upload'
            
            if self.txtPolicy.get()!="":
                ciphertext, aes_key, nonce = self.aes_encrypt()
                encrypted_aes_key = self.cpabe_encrypt(aes_key,nonce)
                encrypted_aes_key = objectToBytes(encrypted_aes_key, group).decode()

                ciphertext = base64.b64encode(ciphertext)

                ciphertext = ciphertext.decode()

                patient_id = json.loads(self.file_content)['patient_id']

                data = {
                    'patient_id' : patient_id,
                    'ciphertext' : ciphertext,
                    'key' : encrypted_aes_key
                }
                status_response = requests.post(url_up, json=data)
                status_response = status_response.json()['data']

                if status_response == "success":
                    messagebox.showinfo("Notice", "Uploaded successful!")
                else:
                    messagebox.showerror("Error", "Failed to upload document!")
            else:
                messagebox.showerror("Error","Policy field must not be empty!")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to upload document! {str(e)}")
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"Failed to decode JSON response! {str(e)}")
