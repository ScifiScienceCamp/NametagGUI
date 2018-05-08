import tkinter as tk
from tkinter import *

class Example(tk.Frame):

	def __init__(self, parent):

		tk.Frame.__init__(self, parent)
		self.label = tk.Label(self, padx=4, pady=4, text="Fields", font='Helvetica 16 bold')
		self.label.grid(row=0, column=0, columnspan=2)

        # Name of column that contains children's first name
		self.first_name_label = tk.Label(self, text="First name:    ", anchor='w')
		self.first_name_label.grid(sticky="W", row=1, column=0)
		self.first_name_field = tk.Entry(self)
		self.first_name_field.insert(END, "FIRST_GIVEN_NAME")
		self.first_name_field.grid(sticky="W", row=1, column=1)

        # Name of column that contains children's last name
		self.last_name_label = tk.Label(self, text="Last name:    ", anchor='w')
		self.last_name_label.grid(sticky="W", row=2, column=0)
		self.last_name_field = tk.Entry(self)
		self.last_name_field.insert(END, "SURNAME")
		self.last_name_field.grid(sticky="W", row=2, column=1)

		self.parent_last_name = tk.Label(self, text="Parent last name:    ", anchor='w')
		self.parent_last_name.grid(sticky="W", row=4, column=0)
		self.parent_last_field = tk.Entry(self)
		self.parent_last_field.insert(END, "P/G_Last_Name")
		self.parent_last_field.grid(sticky="W", row=4, column=1)

		self.parent_first_name = tk.Label(self, text="Parent first name:    ", anchor='w')
		self.parent_first_name.grid(sticky="W", row=3, column=0)
		self.parent_first_field = tk.Entry(self)
		self.parent_first_field.insert(END, "P/G_First_Name")
		self.parent_first_field.grid(sticky="W", row=3, column=1)

		self.parent_phone = tk.Label(self, text="Phone Primary:    ", anchor='w')
		self.parent_phone.grid(sticky="W", row=5, column=0)
		self.parent_phone_field = tk.Entry(self)
		self.parent_phone_field.insert(END, "PHONE_REGULAR")
		self.parent_phone_field.grid(sticky="W", row=5, column=1)

		self.c1_first_name = tk.Label(self, text="C1 First Name:    ", anchor='w')
		self.c1_first_name.grid(sticky="W", row=6, column=0, pady=(6, 0))
		self.c1_first_field = tk.Entry(self)
		self.c1_first_field.insert(END, "C1_First_Name")
		self.c1_first_field.grid(sticky="W", row=6, column=1, pady=(6, 0))

		self.c1_last_name = tk.Label(self, text="C1 Last Name:    ", anchor='w')
		self.c1_last_name.grid(sticky="W", row=7, column=0)
		self.c1_last_field = tk.Entry(self)
		self.c1_last_field.insert(END, "C1_Last_Name")
		self.c1_last_field.grid(sticky="W", row=7, column=1)

		self.c1_phone = tk.Label(self, text="C1 Phone #:    ", anchor='w')
		self.c1_phone.grid(sticky="W", row=8, column=0)
		self.c1_phone_field = tk.Entry(self)
		self.c1_phone_field.insert(END, "C1_Phone_#")
		self.c1_phone_field.grid(sticky="W", row=8, column=1)

		self.c1_pickup = tk.Label(self, text="C1 pickup:    ", anchor='w')
		self.c1_pickup.grid(sticky="W", row=9, column=0)
		self.c1_pickup_field = tk.Entry(self)
		self.c1_pickup_field.insert(END, "C1_Pick-Up")
		self.c1_pickup_field.grid(sticky="W", row=9, column=1)

		self.c2_first_name = tk.Label(self, text="C2 First Name:    ", anchor='w')
		self.c2_first_name.grid(sticky="W", row=10, column=0, pady=(6, 0))
		self.c2_first_field = tk.Entry(self)
		self.c2_first_field.insert(END, "C2_First_Name")
		self.c2_first_field.grid(sticky="W", row=10, column=1, pady=(6, 0))

		self.c2_last_name = tk.Label(self, text="C2 Last Name:    ", anchor='w')
		self.c2_last_name.grid(sticky="W", row=11, column=0)
		self.c2_last_field = tk.Entry(self)
		self.c2_last_field.insert(END, "C2_Last_Name")
		self.c2_last_field.grid(sticky="W", row=11, column=1)

		self.c2_phone = tk.Label(self, text="C2 Phone #:    ", anchor='w')
		self.c2_phone.grid(sticky="W", row=12, column=0)
		self.c2_phone_field = tk.Entry(self)
		self.c2_phone_field.insert(END, "C2_Phone_#")
		self.c2_phone_field.grid(sticky="W", row=12, column=1)

		self.c2_pickup = tk.Label(self, text="C2 Pickup #:    ", anchor='w')
		self.c2_pickup.grid(sticky="W", row=13, column=0)
		self.c2_pickup_field = tk.Entry(self)
		self.c2_pickup_field.insert(END, "C2_Pick-Up")
		self.c2_pickup_field.grid(sticky="W", row=13, column=1)

		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(2, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(2, weight=1)

if __name__ == "__main__":

	root = tk.Tk()
	Example(root).grid(sticky="nsew")
	root.grid_rowconfigure(0, weight=1)
	root.grid_columnconfigure(0, weight=1)

	print(Example(root).parent_last_field.get())

	root.mainloop()
