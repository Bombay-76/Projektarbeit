import tkinter as tk
from tkinter import ttk

"""
    Grafische Oberfläche
"""

root = tk.Tk()
root.title("YouTrack")
root.resizable(True, True)

def center_window(window, width=1280, height=720):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def login_mask():
    login_frame = ttk.Frame(root, padding=30)
    login_frame.pack(expand=True)

    ttk.Label(login_frame, text="Benutzername:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    ttk.Entry(login_frame, textvariable="username_var").grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(login_frame, text="Passwort:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    ttk.Entry(login_frame, textvariable="password_var", show="*").grid(row=1, column=1, padx=10, pady=10)

    status_label = ttk.Label(login_frame, text="")
    status_label.grid(row=2, column=0, columnspan=2)

    # Neuen Frame für die Buttons
    button_frame = ttk.Frame(login_frame)
    button_frame.grid(row=3, column=1, pady=15, sticky="e")

    # Anmelde-Button
    ttk.Button(button_frame, text="Anmelden", command="login").pack(side="left", padx=(0, 5))

    # Registrier-Button
    ttk.Button(button_frame, text="Registrieren", command="register").pack(side="left")



login_mask()
center_window(root)
root.mainloop()