import tkinter as tk
from Fields import Fields
from tkinter import *

class Manager():

    def __init__(self):

        self.root = tk.Tk()
        Fields(self.root).grid(sticky="nsew")
        self.root.geometry("+100+100")

        root2 = tk.Toplevel()
        banana = Label(root2, text="hello world")
        print("root width: " + str(self.root.winfo_reqwidth()))
        x = str(self.root.winfo_reqwidth() + 140)

        print("x: " + x)
        root2.geometry("+"+x+"+100")
        banana.grid(row=0, column=0)

    def get_fields(self):

        return Fields(self.root).get_fields()

if __name__ == "__main__":
    Manager()
    mainloop()
