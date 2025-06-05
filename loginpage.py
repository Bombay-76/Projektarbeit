import tkinter as tk, customtkinter as ctk
from registerpage import RegisterFrame
import database
import os

    #KlasseFürDasDesignDesLoginfensters 
class LoginFrame(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.db = db
        self.parent = parent
        self.container = parent
        self.login_bg()
        self.employee_id = self.tb_ID()
        self.employee_pw = self.tb_PW()
        self.bn_login()
        self.bn_registrieren()

    def login_bg(self):
        fg_frame = ctk.CTkFrame(self.parent, fg_color = "gray85", corner_radius=15)
        fg_frame.place(relx=0.3, rely=0.25, relwidth = 0.4, relheight = 0.45)
        ctk.CTkLabel(
        fg_frame,
        text="YouTrack",
        font=("Arial", 32, "bold"),
        text_color="red"
        ).pack(pady=(10, 0))
        ctk.CTkLabel(fg_frame, text="Anmelden", font=("Arial", 20)).pack(pady=(5, 10))
        return fg_frame

    def tb_ID(self):
        entry_id = ctk.CTkEntry(
            master = self.parent,
            placeholder_text = "Mitarbeiter ID",
            placeholder_text_color = "#ffffff",
            font = ("Arial", 14),
            text_color = "#ffffff",
            height = 30,
            width = 195,
            border_width = 1,
            corner_radius = 15,
            border_color = "#000000",
            bg_color = "gray85",
            fg_color = "#7d7d7d",
            )
        entry_id.place(relx=0.5, rely=0.4, anchor="center")
        return entry_id

    def tb_PW(self):
        entry_pw = ctk.CTkEntry(
            master = self.parent,
            placeholder_text = "Passwort",
            placeholder_text_color = "#ffffff",
            show = "*",
            font = ("Arial", 14),
            text_color = "#ffffff",
            height = 30,
            width = 195,
            border_width = 1,
            corner_radius = 15,
            border_color = "#000000",
            bg_color = "gray85",
            fg_color = "#7d7d7d",
            )
        entry_pw.place(relx=0.5, rely=0.47, anchor="center")
        return entry_pw

    def bn_login(self):
        button_login = ctk.CTkButton(
            master = self.parent,
            text = "Login",
            font = ("undefined", 14),
            text_color = "#ffffff",
            hover = True,
            hover_color = "#949494",
            height = 30,
            width = 95,
            border_width = 1,
            corner_radius = 15,
            border_color = "#000000",
            bg_color = "#D9D9D9",
            fg_color = "gray25",
            command = self.do_login
            )
        button_login.place(relx=0.45, rely=0.6, anchor="center")
        return button_login

    def bn_registrieren(self):
        button_register = ctk.CTkButton(
            master=self.parent,
            text="Registireren",
            font=("undefined", 14),
            text_color="#ffffff",
            hover=True,
            hover_color="#949494",
            height=30,
            width=95,
            border_width=1,
            corner_radius=15,
            border_color="#000000",
            bg_color="#D9D9D9",
            fg_color="gray25",
            command =  lambda:  self.container.show_frame("register")
            )
        button_register.place(relx=0.54, rely=0.6, anchor="center")
        return button_register
    
    def do_login(self):
        mitarbeiter_nr = self.employee_id.get()
        passwort = self.employee_pw.get()
        result = self.db.login(mitarbeiter_nr, passwort)
        if result:
            print("Login erfolgreich!")
            self.container.show_frame("main")

