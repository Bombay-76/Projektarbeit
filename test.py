import tkinter as tk
from tkinter import ttk


def center_window(window, width=1280, height=720):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def login(event=None):
    username = username_var.get()
    password = password_var.get()

    if username == "admin" and password == "admin123":
        show_admin_panel()
    else:
        login_status.config(text="Falscher Benutzername oder Passwort", foreground="red")


def show_admin_panel():
    login_frame.pack_forget()

    # Admin-Bereich anzeigen
    global admin_frame
    admin_frame = ttk.Frame(root, padding=20)
    admin_frame.pack(expand=True)

    global welcome_label
    ttk.Label(admin_frame, text="Admin-Bereich", font=("Arial", 20)).pack(pady=10)
    welcome_label = ttk.Label(admin_frame, text="Willkommen, Admin!", font=("Arial", 14))
    welcome_label.pack(pady=10)

    # Willkommensnachricht nach 3 Sekunden entfernen
    root.after(2000, remove_welcome_message)


def remove_welcome_message():
    welcome_label.destroy()


# Fenster initialisieren
root = tk.Tk()
root.title("YouTrack")
center_window(root)
root.resizable(True, True)
root.bind('<Return>', login)

# Login UI
login_frame = ttk.Frame(root, padding=30)
login_frame.pack(expand=True)

username_var = tk.StringVar()
password_var = tk.StringVar()

ttk.Label(login_frame, text="Mitarbeiter ID:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
ttk.Entry(login_frame, textvariable=username_var).grid(row=0, column=1, padx=10, pady=10)

ttk.Label(login_frame, text="Passwort:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
ttk.Entry(login_frame, textvariable=password_var, show="*").grid(row=1, column=1, padx=10, pady=10)

ttk.Button(login_frame, text="Anmelden", command=login).grid(row=2, column=0, columnspan=2, pady=20)

login_status = ttk.Label(login_frame, text="")
login_status.grid(row=3, column=0, columnspan=2)

root.mainloop()
