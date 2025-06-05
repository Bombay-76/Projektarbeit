#registerpage.py datei 4
import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkFrame
import database

class RegisterFrame(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.de = db
        self.parent = parent
        self.container = parent
        self.bg_register()
        self.lb_register_hint()
        self.entry_name = self.tb_name_input()
        self.entry_surname = self.tb_surname_input()
        self.entry_adress = self.tb_adress_input()
        self.entry_password = self.tb_password_input()
        self.bn_confirm_register()

# Hintergrund-Frame
    def bg_register(self):
        fg_frame = ctk.CTkFrame(self.parent, fg_color="gray85", corner_radius=15)
        fg_frame.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.5)
        ctk.CTkLabel(fg_frame, text="Registrieren", font=("Arial", 20)).pack(pady=10)
        return fg_frame

# Hinweistext
    def lb_register_hint(self):
        lb_hint = ctk.CTkLabel(
            master=self.parent,
            text="Bitte geben Sie Ihre Daten ein:",
            font=("Arial", 14),
            text_color="#000000",
            height=30,
            width=95,
            corner_radius=0,
            bg_color="gray85",
            fg_color="gray85",
        )
        lb_hint.place(relx=0.5, rely=0.34, anchor="center")

# Eingabe Vorname
    def tb_name_input(self):
        tb_input_name = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Vorname",
            placeholder_text_color="#ffffff",
            font=("Arial", 14),
            text_color="#ffffff",
            height=30,
            width=195,
            border_width=1,
            corner_radius=15,
            border_color="#000000",
            bg_color="gray85",
            fg_color="#7d7d7d",
        )
        tb_input_name.place(relx=0.5, rely=0.4, anchor="center")
        return tb_input_name

# Eingabe Nachname
    def tb_surname_input(self):
        entry_surname = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Nachname",
            placeholder_text_color="#ffffff",
            font=("Arial", 14),
            text_color="#ffffff",
            height=30,
            width=195,
            border_width=1,
            corner_radius=15,
            border_color="#000000",
            bg_color="gray85",
            fg_color="#7d7d7d",
        )
        entry_surname.place(relx=0.5, rely=0.47, anchor="center")
        return entry_surname

# Eingabe Adresse
    def tb_adress_input(self):
        entry_adress = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Adresse",
            placeholder_text_color="#ffffff",
            font=("Arial", 14),
            text_color="#ffffff",
            height=30,
            width=195,
            border_width=1,
            corner_radius=15,
            border_color="#000000",
            bg_color="gray85",
            fg_color="#7d7d7d",
        )
        entry_adress.place(relx=0.5, rely=0.54, anchor="center")
        return entry_adress

# Eingabe Passwort
    def tb_password_input(self):
        entry_pw = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Passwort",
            placeholder_text_color="#ffffff",
            font=("Arial", 14),
            text_color="#ffffff",
            height=30,
            width=195,
            border_width=1,
            corner_radius=15,
            border_color="#000000",
            bg_color="gray85",
            fg_color="#7d7d7d",
            show="*"
        )
        entry_pw.place(relx=0.5, rely=0.61, anchor="center")
        return entry_pw

# Registrieren-Button mit Datenbankfunktion
    def bn_confirm_register(self):
        button_conf_register = ctk.CTkButton(
            master=self.parent,
            text="Registrieren",
            font=("Arial", 14),
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
            command=self.register_user  # ✅ ganz wichtig: OHNE Klammern!
        )
        button_conf_register.place(relx=0.5, rely=0.7, anchor="center")
        return button_conf_register


# Registrierung in Datenbank durchführen
    def register_user(self):
        vorname = self.entry_name.get()
        nachname = self.entry_surname.get()
        adresse = self.entry_adress.get()
        passwort = self.entry_password.get()

        if vorname and nachname and adresse and passwort:
            mitarbeiter_nr = vorname[:2] + nachname[:2] + "01"
            self.db.register(mitarbeiter_nr, vorname, nachname, adresse, passwort)
            print("Registrierung erfolgreich")
            self.container.show_frame("login")
        else:
            print("Bitte alle Felder ausfüllen")

