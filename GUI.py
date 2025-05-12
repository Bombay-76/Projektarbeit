import tkinter as tk
from tkinter import ttk
from database import Datenbank

root = tk.Tk()
root.title("YouTrack")
root.geometry("1280x720+0+0")
root.resizable(True, True)

# Zentrum konfigurieren
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

    # Globale Variablen für Frames
login_frame = None
register_frame = None

    # Fenster zentrieren
def center_window(window, width=1280, height=720):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    # Login-Maske
def login_mask():
    global login_frame, register_frame
    if register_frame:
        register_frame.destroy()

    login_frame = ttk.Frame(root, padding=30)
    login_frame.grid(row=0, column=0)

    username_var = tk.StringVar()
    password_var = tk.StringVar()

    ttk.Label(login_frame, text="Benutzername:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    ttk.Entry(login_frame, textvariable=username_var).grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(login_frame, text="Passwort:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    ttk.Entry(login_frame, textvariable=password_var, show="*").grid(row=1, column=1, padx=10, pady=10)

    status_label = ttk.Label(login_frame, text="")
    status_label.grid(row=2, column=0, columnspan=2)

    button_frame = ttk.Frame(login_frame)
    button_frame.grid(row=3, column=0, columnspan=2, pady=15)

    ttk.Button(button_frame, text="Anmelden", command=lambda: print("Login")).pack(side="left", padx=(0, 5))
    ttk.Button(button_frame, text="Registrieren", command=register_mask).pack(side="left")

    # Registrierungs-Maske
def register_mask():
    global login_frame, register_frame
    if login_frame:
        login_frame.destroy()

    register_frame = ttk.Frame(root, padding=30)
    register_frame.grid(row=0, column=0)

    register_frame.grid_columnconfigure(0, weight=1)
    register_frame.grid_columnconfigure(1, weight=1)

    name_var = tk.StringVar()
    vorname_var = tk.StringVar()
    geburtsdatum_var = tk.StringVar()
    adresse_var = tk.StringVar()
    passwort_var = tk.StringVar()

    ttk.Label(register_frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(register_frame, textvariable=name_var, width=30).grid(row=0, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(register_frame, text="Vorname:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(register_frame, textvariable=vorname_var, width=30).grid(row=1, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(register_frame, text="Adresse:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(register_frame, textvariable=adresse_var, width=30).grid(row=3, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(register_frame, text="Passwort:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(register_frame, textvariable=passwort_var, show="*", width=30).grid(row=4, column=1, padx=10, pady=5, sticky="w")

    def speichern():
        Datenbank().register()
        login_mask()  # Zurück zur Anmeldemaske

    # Speichern-Button zentriert unter den Eingabefeldern
    ttk.Button(register_frame, text="Speichern", command=speichern)\
        .grid(row=5, column=0, columnspan=2, pady=20)


# Start
login_mask()
center_window(root)
root.mainloop()
