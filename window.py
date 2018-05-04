import tkinter as tk
from tkinter import *

class Example(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, padx=4, pady=4, text="Fields", font='Helvetica 16 bold')
        label.grid(row=1, columnspan=2)

        first_name_label = tk.Label(self, text="Child's first name:    ", anchor='w')
        first_name_label.grid(sticky="W", row=2, column=1)

        first_name_field = tk.Entry(self)
        first_name_field.insert(END, "CHILD_FIRST_NAME")
        first_name_field.grid(sticky="W", row=2, column=2)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

if __name__ == "__main__":

    root = tk.Tk()
    Example(root).grid(sticky="nsew")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()
