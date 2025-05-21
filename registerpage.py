import customtkinter as ctk, tkinter as tk

class RegisterFrame(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)
        self.parent = parent


        self.register_bg()

    def register_bg(self):
        fg_frame = ctk.CTkFrame(self.parent, fg_color="gray85", corner_radius=15)
        fg_frame.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.45)
        ctk.CTkLabel(fg_frame, text="Registrieren", font= ("Arial", 20)).pack(pady=10)
        return fg_frame