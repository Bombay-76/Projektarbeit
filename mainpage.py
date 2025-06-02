import customtkinter as ctk
import tkinter as tk
import database

obj_db = database.Datenbank()

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.container = parent
        self.bg_main()
        self.lb_hint()
        self.tb_project_id()
        self.tb_project_name()
        self.tb_customer_nr()
        self.tb_work_time()
        self.bn_add_project()
        self.bn_log_time()

    def bg_main(self):
        fg_frame = ctk.CTkFrame(self.parent, fg_color="gray85", corner_radius=15)
        fg_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        ctk.CTkLabel(fg_frame, text="Projektverwaltung", font=("Arial", 20)).pack(pady=10)

    def lb_hint(self):
        label = ctk.CTkLabel(
            master=self.parent,
            text="Projekte hinzufügen oder Zeit erfassen:",
            font=("Arial", 14),
            text_color="#000000",
            bg_color="gray85"
        )
        label.place(relx=0.5, rely=0.3, anchor="center")

    def tb_project_id(self):
        self.entry_project_id = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Projekt-ID",
            font=("Arial", 14),
            width=200
        )
        self.entry_project_id.place(relx=0.5, rely=0.4, anchor="center")

    def tb_project_name(self):
        self.entry_project_name = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Projektname",
            font=("Arial", 14),
            width=200
        )
        self.entry_project_name.place(relx=0.5, rely=0.45, anchor="center")

    def tb_customer_nr(self):
        self.entry_customer_nr = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Kundennummer",
            font=("Arial", 14),
            width=200
        )
        self.entry_customer_nr.place(relx=0.5, rely=0.5, anchor="center")

    def tb_work_time(self):
        self.entry_work_time = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Gearbeitete Stunden (Projekt-ID, Stunden)",
            font=("Arial", 14),
            width=250
        )
        self.entry_work_time.place(relx=0.5, rely=0.6, anchor="center")

    def bn_add_project(self):
        btn = ctk.CTkButton(
            master=self.parent,
            text="Projekt hinzufügen",
            command=self.add,
            font=("Arial", 14),
            width=150
        )
        btn.place(relx=0.4, rely=0.7, anchor="center")

    def bn_log_time(self):
        btn = ctk.CTkButton(
            master=self.parent,
            text="Zeit erfassen",
            command=self.arbeitszeit,
            font=("Arial", 14),
            width=150
        )
        btn.place(relx=0.6, rely=0.7, anchor="center")

    def add(self):
        projekt_id = self.entry_project_id.get()
        projektname = self.entry_project_name.get()
        kunden_nr = self.entry_customer_nr.get()
        if projekt_id and projektname and kunden_nr:
            obj_db.add(projekt_id, projektname, kunden_nr)
            print("Projekt hinzugefügt")

    def arbeitszeit(self):
        try:
            projekt_id, stunden = self.entry_work_time.get().split(",")
            obj_db.arbeitszeit(projekt_id.strip(), float(stunden.strip()))
            print("Zeit erfasst")
        except:
            print(f"Da hat etwas nicht geklappt")

