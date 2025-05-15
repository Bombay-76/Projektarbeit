from styles import *


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTrack")

        self.root.resizable(True, True)

        self.window_width = 1280
        self.window_height = 720

        self.center_window()
        self.login_mask()


    def center_window(self):

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width - self.window_width) / 2)
        y = int((screen_height - self.window_height) / 2)

        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")


    def login_mask(self):
        login_frame()
        tb_ID()
        tb_PW()
        bn_login()
        bn_registrieren()


if __name__ == "__main__":
    app = GUI(root)
    root.mainloop()