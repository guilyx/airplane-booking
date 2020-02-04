'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 02/02/2020
@brief : airplane reservation program
'''


import sys
from os import path
from os import system
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from lib.booker import Booker
from lib.passenger import Passenger
import string, random


def main():
    maestro = Booker()
    name_list = []
    passports = []
    passengers = []
    for i in range(50):
        name_list.append(''.join(random.choice(string.ascii_lowercase) for _ in range(7)))
        passports.append(random.randint(1000, 10000))
        passengers.append(Passenger(name_list[i], passports[i]))

    maestro.reserve_ticket(passengers[0])

    print(maestro.flight_dtb["New York"].print_passenger())
    print(passengers[0].print_info())





if __name__ == "__main__":
    main()