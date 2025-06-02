#GUI Datei 6
from loginpage import *
import database
from mainpage import MainFrame
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("YouTrack")
        self.resizable(True, True)
        self.window_width = 1280
        self.window_height = 720
        self.center_window()
        ctk.set_appearance_mode("System")

        self.frame = tk.Frame(self)
        self.frame.pack(expand=True)

        self.show_frame("login")

    def show_frame(self, frame_name):
        if self.frame is not None:
            self.frame.destroy()

        if frame_name == "login":
            self.frame = LoginFrame(self)
        elif frame_name == "register":
            self.frame = RegisterFrame(self)
        elif frame_name == "main":
            self.frame = MainFrame(self)
        else:
            print("ungültig")

        self.frame.pack(expand=True)


    def center_window(self):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width - self.window_width) / 2)
        y = int((screen_height - self.window_height) / 2)

        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def do_login(self):
        mitarbeiter_nr = self.employee_id.get()
        passwort = self.employee_pw.get()
        result = obj_db.login(mitarbeiter_nr, passwort)
        if result:
            print("Login erfolgreich!")
            self.container.show_frame("main")


if __name__ == "__main__":
    app = GUI()
    app.mainloop()