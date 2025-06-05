#GUI.py datei 6 
import database
from loginpage import *
from mainpage import MainFrame
from Projectinsightpage import Project_insight_Frame

class GUI(tk.Tk):#KlasseFürGUI
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.db = database.Datenbank()
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
            self.frame = LoginFrame(self, self.db)#Self.db ÜbergibtDatenbank
        elif frame_name == "register":
            self.frame = RegisterFrame(self, self.db)
        elif frame_name == "main":
            self.frame = MainFrame(self,self.db)
        elif frame_name == "project":
            self.frame = Project_insight_Frame(self, self.db)
        else:
            print("ungültig")
            return

        self.frame.pack(expand=True)

    def center_window(self):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width - self.window_width) / 2)
        y = int((screen_height - self.window_height) / 2)

        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    #def do_login(self):
    #    mitarbeiter_nr = self.employee_id.get()
     #   passwort = self.employee_pw.get()
      #  result = self.db.login(mitarbeiter_nr, passwort)
       # if result:
        #    print("Login erfolgreich!")
         #   self.container.show_frame("main")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()