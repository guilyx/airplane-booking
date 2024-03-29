"""
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 14/02/2020
@brief : airplane reservation gui
"""

import tkinter as tk
from lib.booker import Booker


class Interface(tk.Frame):
    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=500, height=300, **kwargs)
        self.grid(sticky="nsew")
        self.option_add("*Font", "Helvetica 16")
        self.option_add("*Background", "light blue")

        self.option_add("*selectBackground", "orange")
        self.option_add("*selectForeground", "black")
        self.config(background="light blue")

        self.startup_menu()

    def startup_menu(self):
        # Création de nos widgets
        self.clear()
        message = tk.Label(
            self, text="Welcome on my first GUI\n", font=("Helvetica", 12, "bold")
        )
        message.grid(column=0, row=0)

        message2 = tk.Label(self, text="On this API you will be able to :\n")
        message2.grid(column=0, row=2)

        options = dict()
        options[0] = "   - Book tickets from a list of destinations."
        options[1] = "   - Cancel tickets from the list of tickets you own."
        options[
            2
        ] = "   - Display info on Planes, Tickets, Destinations and yourself.\n"
        for i in range(3):
            tk.Label(self, text=options[i]).grid(column=0, row=3 + i, sticky="w")

        self.start_button = tk.Button(
            self, text="Click to Start", fg="green", command=self.get_id
        )
        self.start_button.grid(column=0, row=9, sticky="sw")

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.grid(column=4, row=9, sticky="se")

        self.restart_button = tk.Button(self, text="Restart", command=self.startup_menu)
        self.restart_button.grid(column=3, row=9, sticky="se")

    def get_id(self):
        self.clear()
    
        message2 = tk.Label(self, text="Enter your IDs")
        message2.grid(column=0, row=2)

        message3 = tk.Label(self, text="Name")
        message3.grid(column=3, row=1)

        message4 = tk.Label(self, text="Passport Num.")
        message4.grid(column=4, row=1)

        self.name_entry = tk.Entry(self, width=10, validatecommand=self.validate_name)
        self.name_entry.grid(column=3, row=2)

        self.passport_entry = tk.Entry(
            self, width=10, show="*", validatecommand=self.validate_passport
        )
        self.passport_entry.grid(column=4, row=2)

        ok_button = tk.Button(self, text="Send Entry", fg="red", command=self.send_id)
        ok_button.grid(column=5, row=2)

    def send_id(self):
        self.name = self.name_entry.get()
        self.passport = self.passport_entry.get()

        next_button = tk.Button(self, text="Next", fg="green", command=self.main_menu)
        next_button.grid(column=0, row=9, sticky = "sw")

    def main_menu(self):
        self.clear()

        message = tk.Label(self, text="Hello " + self.name + ", ")
        message.grid(column=0, row=0, sticky = "nw")

        message3 = tk.Label(
            self,
            text="Welcome to our main menu. Please select what you want to do."
        )
        message3.grid(column=0, row=1, sticky = "nw")

        bttn_opt = []
        descr_labels = []
        descr = ""
        for i in range(4):
            if(i == 0):
                descr = "------------------ Book Tickets"
            elif(i == 1):
                descr = "------------------ Cancel Tickets"
            elif(i == 2):
                descr = "------------------ Select Ticket and Display its information"
            elif(i == 3):
                descr = "------------------ Display your information"

            descr_labels.append(tk.Label(self, text=descr).grid(column=0, row=(i+2), sticky="w"))
            bttn_opt.append(tk.Button(self, text="Choice " + str(i+1)).grid(column=0, row=(i+2), sticky="w"))

    def validate_name(self):
        name = self.name_entry.get()
        is_str = name.isalnum()
        return is_str

    def validate_passport(self):
        passport = self.passport_entry.get()
        is_num = passport.isdigit()
        return is_num

    def clear(self):
        slaves = self.grid_slaves()
        for elem in slaves:
            if elem == self.exit_button or elem == self.restart_button:
                continue
            else:
                elem.destroy()
