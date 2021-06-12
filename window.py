from chaild import ChaildWindow
from tkinter import *
from chaild import ChaildWindow


class Window:
    def __init__(self, width, height, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.root.iconbitmap("icon\icon.ico")

        self.label = Label(self.root, text="meow")

    def run(self):
        self.draw_widget()
        self.root.mainloop()

    def draw_widget(self):
        self.label.pack()

    def create_child(self, width, height, title):

        ChaildWindow(self.root, width, height, title)
