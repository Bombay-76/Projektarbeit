import tkinter as tk, customtkinter as ctk

root = tk.Tk()

def login_frame():
    fg_frame = ctk.CTkFrame(root, fg_color="gray85", corner_radius=15)
    fg_frame.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.45)
    ctk.CTkLabel(fg_frame, text="Anmelden", font= ("Arial", 20)).pack(pady=10)
    return fg_frame

def tb_ID():
    entry_id = ctk.CTkEntry(
        master=root,
        placeholder_text="Mitarbeiter ID",
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
    entry_id.place(relx=0.5, rely=0.4, anchor="center")
    return entry_id

def tb_PW():
    entry_pw = ctk.CTkEntry(
        master=root,
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
        )
    entry_pw.place(relx=0.5, rely=0.47, anchor="center")
    return entry_pw

def bn_login():
    button_login = ctk.CTkButton(
        master=root,
        text="Login",
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
        #command =
        )
    button_login.place(relx=0.45, rely=0.6, anchor="center")
    return button_login

def bn_registrieren():
    button_register = ctk.CTkButton(
        master=root,
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
        )
    button_register.place(relx=0.54, rely=0.6, anchor="center")
    return button_register