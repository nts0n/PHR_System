import tkinter as ctk
from tkinter import messagebox

class Application(ctk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PHR Secure Demo")
        self.geometry("900x700")

        self.frames = {}
        self.current_frame = None
        
        self.create_frames()

    def create_frames(self):
        import ClassContainer

        frame1 = ClassContainer.LoginForm(self)
        frame2 = ClassContainer.MenuForm(self)
        frame3 = ClassContainer.RetrieveForm(self)
        frame4 = ClassContainer.UploadForm(self)

        self.frames[ClassContainer.LoginForm] = frame1
        self.frames[ClassContainer.MenuForm] = frame2
        self.frames[ClassContainer.RetrieveForm] = frame3
        self.frames[ClassContainer.UploadForm] = frame4
        
        frame1.pack()
        self.current_frame = frame1

    def show_frame(self, frame_class):
        new_frame = self.frames[frame_class]
        new_frame.pack()
        
        if self.current_frame is not None:
            self.current_frame.pack_forget()
            
        self.current_frame = new_frame