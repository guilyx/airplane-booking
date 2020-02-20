"""
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 02/02/2020
@brief : airplane reservation program
"""


import sys
from os import path
from os import system

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from lib.booker import Booker
from lib.passenger import Passenger
from lib.gui import Interface
import string, random
import tkinter as tk


def main():
    maestro = Booker()

    while maestro.exit == False:
        maestro.main_menu()

def frame():
    window = tk.Tk()
    window.title("Booking Menu")
    window.geometry('500x300')
    frame = Interface(window)

    frame.mainloop()
    frame.destroy()


if __name__ == "__main__":
    frame()
