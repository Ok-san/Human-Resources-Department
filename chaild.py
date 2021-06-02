from tkinter import *


class ChaildWindow:
    def __init__(self, perent, width, height, title):
        self.root = Toplevel(perent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.root.iconbitmap("icon\icon.ico")

        self.focus()

    def focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
