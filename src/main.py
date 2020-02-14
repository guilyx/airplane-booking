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
import string, random


def main():
    maestro = Booker()

    while maestro.exit == False:
        maestro.main_menu()


if __name__ == "__main__":
    main()
