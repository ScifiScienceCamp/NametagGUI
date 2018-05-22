import tkinter as tk
import os
from os.path import isfile, join
from Fields import Fields
from tkinter import *

class Manager():

    def __init__(self):

        self.root = tk.Tk()
        Fields(self.root).grid(sticky="nsew")
        self.root.geometry("+100+100")

        root2 = tk.Toplevel()
        banana = Label(root2, text="hello world")
        x = str(self.root.winfo_reqwidth() + 140)

        root2.geometry("+"+x+"+100")
        banana.grid(row=0, column=0)

        self.camps = []
        dirs = getDirectories(getFilepath("."))


    def get_fields(self):

        return Fields(self.root).get_fields()

def getDirectories(path):
    return [f for f in os.listdir(path) if not isfile(join(path, f))
    and not f == "data" and not f=='EH' and not f=='GP' and not f=='__pycache__']

# This function returns the absolute filepath for the given string
# This means we can use relative paths and run the program from anywhere
def getFilepath(file):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = file#"template.docx"
    return os.path.join(script_dir, rel_path)

if __name__ == "__main__":
    Manager()
    mainloop()
