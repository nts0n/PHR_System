import tkinter as ctk
from tkinter import messagebox

class MenuForm(ctk.Frame):
    def __init__(self, master):
        import ClassContainer
        super().__init__(master)
        self.buttonFrame = ctk.Frame(self)
        self.buttonFrame.columnconfigure(0, weight=1)

        self.uploadBtn = ctk.Button(self.buttonFrame, text="Upload", font=("Arial",22), command=lambda: [self.check(master)])
        self.uploadBtn.grid(column=0,row=0,padx=50,pady=100,sticky=ctk.W)

        self.downloadBtn = ctk.Button(self.buttonFrame, text="Retrieve / Download", font=("Arial",22), command=lambda: [master.show_frame(ClassContainer.RetrieveForm)])
        self.downloadBtn.grid(column=4, row=0,padx=50,pady=100,sticky=ctk.W)

        self.logoutBtn = ctk.Button(self, text="Logout", font=("Arial",18), command=lambda: [master.show_frame(ClassContainer.LoginForm)])
        self.logoutBtn.pack(side="top",anchor="ne")

        self.buttonFrame.pack(padx=50,pady=50,fill="x")
    def check(self, master):
        from ClassContainer import user_attribute, UploadForm
        if('PATIENT' in user_attribute) or ('DOCTOR' in user_attribute):
            master.show_frame(UploadForm)
        else:
            messagebox.showerror("ERROR!", "You are not allowed to upload document!")