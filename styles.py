import tkinter as tk, customtkinter as ctk


root = tk.Tk()

def login_frame():
    fg_frame = ctk.CTkFrame(root, fg_color="gray85", corner_radius=15)
    fg_frame.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.45)
    ctk.CTkLabel(fg_frame, text="Anmelden", font= ("Arial", 20)).pack(pady=10)
    return fg_frame

def tb_ID():
    Entry_id2 = ctk.CTkEntry(
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
    Entry_id2.place(relx=0.5, rely=0.4, anchor="center")
    return Entry_id2

def tb_PW():
    Entry_id2 = ctk.CTkEntry(
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
    Entry_id2.place(relx=0.5, rely=0.47, anchor="center")
    return Entry_id2

def bn_login():
    Button_id3 = ctk.CTkButton(
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
        )
    Button_id3.place(relx=0.45, rely=0.6, anchor="center")
    return Button_id3

def bn_registrieren():
    Button_id3 = ctk.CTkButton(
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
    Button_id3.place(relx=0.54, rely=0.6, anchor="center")
    return Button_id3