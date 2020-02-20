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

        # Création de nos widgets
        message = tk.Label(self, text="Welcome on my first GUI")
        message.grid(column=4, row=0)

        message2 = tk.Label(self, text="Enter your IDs")
        message2.grid(column=0, row=2)

        message3 = tk.Label(self, text="Name")
        message3.grid(column=3, row=1)

        message4 = tk.Label(self, text="Passport Num.")
        message4.grid(column=4, row=1)

        self.name_entry = tk.Entry(self, width=10, validatecommand=self.validate_name)
        self.name_entry.grid(column=3, row=2)

        self.passport_entry = tk.Entry(self, width=10, show="*", validatecommand=self.validate_passport)
        self.passport_entry.grid(column=4, row=2)

        self.ok_button = tk.Button(
            self, text="Send Entry", fg="red", command=self.send_id
        )
        self.ok_button.grid(column=5, row=2)

        self.bouton_quitter = tk.Button(self, text="Exit", command=self.quit)
        self.bouton_quitter.grid(column=4, row=7)

    def send_id(self):
        self.name = self.name_entry.get()
        self.passport = self.passport_entry.get()

    def validate_name(self):
        name = self.name_entry.get()
        is_str = name.isalnum()
        return(is_str)

    def validate_passport(self):
        passport = self.passport_entry.get()
        is_num = passport.isdigit()
        return(is_num)
