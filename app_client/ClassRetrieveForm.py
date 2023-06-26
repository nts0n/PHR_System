import tkinter as ctk
from tkinter import messagebox, filedialog
import json
import requests
import base64
from Crypto.Random import get_random_bytes
from charm.core.engine.util import objectToBytes,bytesToObject
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1
from cryptography.hazmat.primitives.ciphers.aead import AESGCM



class RetrieveForm(ctk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.create_ui(master)

    def create_ui(self,master):
        import ClassContainer

        # create back button
        self.backBtn = ctk.Button(self, text="Back", font=("Arial",12),command=lambda: [master.show_frame(ClassContainer.MenuForm)])
        self.backBtn.place(x=20,y=20)

        # create logout button
        self.logoutBtn = ctk.Button(self, text="Logout", font=("Arial",12),command=lambda: [master.show_frame(ClassContainer.LoginForm)])
        self.logoutBtn.place(x=800,y=20)

        # create title label
        self.titleLabel = ctk.Label(self, text="Retrieve PHR Document", font=("Arial",26))
        self.titleLabel.pack(pady=(80,10))

        # create search frame
        self.searchLabel = ctk.Label(self, text="Enter patient's id: ", font=("Arial",20))
        self.searchLabel.pack(anchor="center")

        self.txtSearch = ctk.Entry(self,width=100)
        self.txtSearch.pack(pady=(10,10))

        self.searchBtn = ctk.Button(self,text="Search",font=("Arial",14),command=lambda: [self.search_event()])
        self.searchBtn.pack()

        # create content (document) view text box
        self.txtDocumentView = ctk.Listbox(self,font=("Arial",12),width=100, height=50)
        # self.txtDocumentView.place(x=150,y=150)
        self.txtDocumentView.pack(padx=50,pady=(20,100))

        # create download button
        self.downloadBtn = ctk.Button(self,text="Download",font=("Arial",14), command=lambda: [self.download_event()])
        self.downloadBtn.place(x=400,y=600)
        # self.downloadBtn.pack(pady=(0,50))

    def search_event(self):
        try:
            
            from ClassContainer import url
            id = self.txtSearch.get()

            # Retrieve data from Azure:
            search_url = url + 'search'
            payload = {'patient_id': id}
            status_response = requests.post(search_url, json=payload)
            full_data = status_response.json()
            name_data = full_data['key_value']
            #self.txtDocumentView.delete(1.0, ctk.END)
            if name_data:
                for document in name_data:
                    self.txtDocumentView.insert(ctk.END,str(document))
            else:
                messagebox.showerror("Error","Document not found!")
        except:
            messagebox.showerror("Error","Failed to retrieve data!")

    def download_event(self):
        try:
            from ClassContainer import url

            group = PairingGroup('MNT224')
            cpabe = CPabe_BSW07(group)
            hyb_abe = HybridABEnc(cpabe, group)

            selected_file = self.txtDocumentView.curselection()
            if (selected_file == None):
                messagebox.showerror("Error!!", "Please choose a file!")
                return
            filename = self.txtDocumentView.get(selected_file[0])
            
            
            download_url = url + 'download'
            
            payload = {
                'filename' : filename,
            }
            
            request = requests.post(download_url, json=payload)
            response_data = request.json()
            ciphertext = response_data['ciphertext'].encode()
            ciphertext = base64.b64decode(ciphertext)
            
            key_aes_cipher = response_data['key'].encode()
            key_aes_cipher = bytesToObject(key_aes_cipher, group)

            user_secret_key = response_data['user_secret_key'].encode()
            user_secret_key = bytesToObject(user_secret_key, group)

            master_pk = response_data['master_pk'].encode()
            master_pk = bytesToObject(master_pk, group)


            key_aes_dec =  hyb_abe.decrypt(master_pk, user_secret_key, key_aes_cipher)
            key_arr = key_aes_dec.split(b',')

            key_aes = key_arr[0]
            nonce = key_arr[1]

            aes = AESGCM(key_aes)
            data = aes.decrypt(nonce=nonce,data=ciphertext,associated_data=None)

            document = json.loads(data.decode())

            dest_dir = filedialog.askdirectory()
                
            # document["_id"] = str(document["_id"]) # parse to string for json.dump()
            document_id = document['patient_id']
                
            file_name = f"{dest_dir}/doc_{str(document_id)}.json" # name the downloaded file
            
            with open(file_name, 'w') as file:
                json.dump(document, file, indent=4)
            messagebox.showinfo("Notice","Downloaded successfully!")
        except :
            messagebox.showerror("Error","Failed to download document!")
