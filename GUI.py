"""
    Grafische Oberfläche
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
w = 1280
h = 720

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Zeiterfassungssystem")

root.mainloop()