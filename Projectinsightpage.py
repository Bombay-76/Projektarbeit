import customtkinter as ctk
import tkinter as tk
import database

class Project_insight_Frame(tk.Frame):
    def __init__(self, parent,db):
        super().__init__(parent)
        self.db = db
        self.parent = parent
        self.container = parent
        self.bg_project_view()
        self.lb_title()
        self.tb_filter_kundennr()
        self.bn_filter()
        self.bn_show_all()
        self.bn_back()
        self.lb_output = self.result_box()

    def bg_project_view(self):
        fg_frame = ctk.CTkFrame(self.parent, fg_color="gray85", corner_radius=15)
        fg_frame.place(relx=0.1, rely=0.15, relwidth=0.75, relheight=0.7)

    def lb_title(self):
        ctk.CTkLabel(
            master=self.parent,
            text="Projektübersicht",
            font=("Arial", 20),
            text_color="#000000",
            bg_color="gray85"
        ).place(relx=0.5, rely=0.18, anchor="center")

    def tb_filter_kundennr(self):
        self.entry_filter = ctk.CTkEntry(
            master=self.parent,
            placeholder_text="Kundennummer",
            font=("Arial", 14),
            width=200
        )
        self.entry_filter.place(relx=0.5, rely=0.28, anchor="center")

    def bn_filter(self):
        btn = ctk.CTkButton(
            master=self.parent,
            text="Filtern",
            command=self.show_filtered,
            font=("Arial", 14),
            width=120
        )
        btn.place(relx=0.42, rely=0.35, anchor="center")

    def bn_show_all(self):
        btn = ctk.CTkButton(
            master=self.parent,
            text="Alle Projekte",
            command=self.show_all,
            font=("Arial", 14),
            bg_color="#D9D9D9",
            fg_color="gray25",            
            width=120
        )
        btn.place(relx=0.58, rely=0.35, anchor="center")

    def bn_back(self):
        btn = ctk.CTkButton(
            master=self.parent,
            text="Zurück",#IchBekommeDenButtonAufDerMainPageNichtWeg:(
            command=lambda: self.container.show_frame("main"),
            font=("Arial", 14),
            bg_color="#D9D9D9",
            fg_color="gray25",            
            width=120
        )
        btn.place(relx=0.5, rely=0.8, anchor="center")

    def result_box(self):
        box = tk.Text(
            master=self.parent,
            height=15,
            width=100,
            bg="#f0f0f0",
            fg="black",
            font=("Arial", 10)
        )
        box.place(relx=0.5, rely=0.6, anchor="center")
        return box

    def show_all(self):
        self.lb_output.delete("1.0", tk.END)
        results = self.db.insight()
        for row in results:
            self.lb_output.insert(tk.END, f"{row}\n")

    def show_filtered(self):
        kundennr = self.entry_filter.get()
        self.lb_output.delete("1.0", tk.END)
        results = self.db.filter(kundennr)
        for row in results:
            self.lb_output.insert(tk.END, f"{row}\n")

