import tkinter as ctk
from tkinter import messagebox
import hashlib
import json
import logging
import requests

class LoginForm(ctk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_ui()

    def create_ui(self):
        self.titleLabel = ctk.Label(
            self, text="Login Form", font=("Arial", 26))
        self.titleLabel.pack(padx=50, pady=20)

        self.loginFrame = ctk.Frame(self)

        self.usernameLabel = ctk.Label(
            self.loginFrame, text="Username:", font=("Arial", 22))
        self.usernameLabel.pack(pady=(20, 0))

        self.txtUsername = ctk.Entry(
            self.loginFrame, font=("Arial", 18), width=100)
        self.txtUsername.pack(padx=200, pady=(0, 20))

        self.passwordLabel = ctk.Label(
            self.loginFrame, text="Password:", font=("Arial", 22))
        self.passwordLabel.pack()

        self.txtPassword = ctk.Entry(
            self.loginFrame, font=("Arial", 18), show="*", width=100)
        self.txtPassword.pack(padx=200)

        self.loginBtn = ctk.Button(
            self.loginFrame, text="Login", font=("Arial", 22), command=self.login_event)
        
        self.loginBtn.pack(padx=30, pady=30)

        self.loginFrame.pack(padx=30, pady=(0, 30), fill="both", expand=True)

    def login_event(self):
        import ClassContainer
        from ClassContainer import url, ssl_context
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        
        data = {
            'username': username,
            'password': hashlib.sha3_256(password.encode("utf-8")).hexdigest()
        }

        get_log = url + 'login'
        status_response = requests.post(get_log, json=data)
        
        if status_response.content.decode() == "false":
            messagebox.showerror("Error","Failed to login!")
        else:
            key_response = status_response.json()
            
            ClassContainer.user_attribute = key_response["attributes"]
            
            self.master.show_frame(ClassContainer.MenuForm)
