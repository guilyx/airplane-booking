"""
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 02/02/2020
@brief : airplane reservation program
"""


import sys
import random
import string
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from lib.passenger import Passenger
from lib.booker import Booker
from lib.flight import Flight

def alpha_or_string(string):
    if (all(x.isalpha() for x in string)) or any(x.isspace() for x in string):
        return True
    else:
        return False

def test_overbooking():
    maestro = Booker()
    name_list = []
    passports = []
    passengers = []
    for i in range(random.randint(500, 5000)):
        name_list.append(
            "".join(random.choice(string.ascii_lowercase) for _ in range(7))
        )
        passports.append(random.randint(1000, 10000))
        passengers.append(Passenger(name_list[i], passports[i]))
        maestro.reserve_ticket(passengers[i], True)
    
    for elem in maestro.destinations:
        assert(maestro.flight_dtb[elem].max >= len(maestro.flight_dtb[elem].passenger_list))

def test_registered_passenger():
    maestro = Booker()
    name_list = []
    passports = []
    passengers = []
    for i in range(random.randint(500, 5000)):
        name_list.append(
            "".join(random.choice(string.ascii_lowercase) for _ in range(7))
        )
        passports.append(random.randint(1000, 10000))
        passengers.append(Passenger(name_list[i], passports[i]))
        maestro.reserve_ticket(passengers[i], True)
    
    for elem in maestro.destinations:
        flight = maestro.flight_dtb[elem]
        for elem in flight.passenger_list:
            assert(elem in maestro.passenger_dtb[x] for x in passports)


def test_valid_destinations():
    maestro = Booker()
    
    for elem in maestro.destinations:
        assert(alpha_or_string(elem) == True)

def test_valid_flight():
    maestro = Booker()
    
    for elem in maestro.destinations:
        flight = maestro.flight_dtb[elem]
        dest = flight.destination
        assert(alpha_or_string(dest) == True)