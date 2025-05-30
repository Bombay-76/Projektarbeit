from loginpage import *#gui

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
        if (frame_name == "login"):
            self.frame = LoginFrame(self)
        elif (frame_name == "register"):
            self.frame = RegisterFrame(self)
        else:
            print("Invalid frame name")

    def center_window(self):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width - self.window_width) / 2)
        y = int((screen_height - self.window_height) / 2)

        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")


if __name__ == "__main__":
    app = GUI()
    app.mainloop()