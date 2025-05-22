import customtkinter
from tkinter import *
import tkinter as tk


#MainFrame
window = Tk()
window.title("Tkinter")
window.geometry("800x350")
window.configure(bg="#FFFFFF")

def insight():
    Button_id1 = customtkinter.CTkButton(
        master=window,
        text="Projekte ansehen",
        font=("undefined", 14),
        text_color="#000000",
        hover=True,
        hover_color="#949494",
        height=30,
        width=128,
        border_width=1,
        corner_radius=16,
        border_color="#000000",
        bg_color="#FFFFFF",
        fg_color="#F0F0F0",
        )
    Button_id1.place(x=10, y=10)
    return Button_id1
    
def delete():

    Button_id3 = customtkinter.CTkButton(
        master=window,
        text="Projekt löschen",
        font=("undefined", 14),
        text_color="#000000",
        hover=True,
        hover_color="#949494",
        height=30,
        width=128,
        border_width=1,
        corner_radius=16,
        border_color="#000000",
        bg_color="#FFFFFF",
        fg_color="#F0F0F0",
        )
    Button_id3.place(x=10, y=110)
    return Button_id3

def add():
    Button_id2 = customtkinter.CTkButton(
        master=window,
        text="Projekte hinzufügen",
        font=("undefined", 14),
        text_color="#000000",
        hover=True,
        hover_color="#949494",
        height=30,
        width=128,
        border_width=1,
        corner_radius=16,
        border_color="#000000",
        bg_color="#FFFFFF",
        fg_color="#F0F0F0",
        )
    Button_id2.place(x=10, y=60)
    return Button_id2

def close():
    Button_id5 = customtkinter.CTkButton(
        master=window,
        text="Abmelden",
        font=("undefined", 14),
        text_color="#000000",
        hover=True,
        hover_color="#949494",
        height=30,
        width=128,
        border_width=1,
        corner_radius=16,
        border_color="#000000",
        bg_color="#FFFFFF",
        fg_color="#F0F0F0",
        )
    Button_id5.place(x=660, y=310)
    return Button_id5

def bar():
    root = tk.Tk()
    black_bar = tk.Frame(root, bg="black", height=30)
    black_bar.pack(fill="x", side="top")

insight()
delete()
add()
close()
bar()


#run the main loop
window.mainloop()