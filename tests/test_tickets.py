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


def checkIfDuplicates(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


def test_ticket_number():
    booker = Booker()
    p1 = Passenger("Norbert", 101)
    booker.reserve_ticket(p1, True)
    assert len(booker.ticket_list) == 1


def test_duplicates_tickets():
    maestro = Booker()
    name_list = []
    passports = []
    passengers = []
    for i in range(50):
        name_list.append(
            "".join(random.choice(string.ascii_lowercase) for _ in range(7))
        )
        passports.append(random.randint(1000, 10000))
        passengers.append(Passenger(name_list[i], passports[i]))
        maestro.reserve_ticket(passengers[i], True)
    assert checkIfDuplicates(maestro.ticket_list) == False


def test_duplicates_passports():
    maestro = Booker()
    name_list = []
    passports = []
    passengers = []
    for i in range(50):
        name_list.append(
            "".join(random.choice(string.ascii_lowercase) for _ in range(7))
        )
        passport_number = random.randint(1000, 10000)
        while passport_number in passports:
            passport_number = random.randint(1000, 10000)
        passports.append(passport_number)
        passengers.append(Passenger(name_list[i], passports[i]))
        maestro.reserve_ticket(passengers[i], True)
    assert checkIfDuplicates(passports) == False


def test_duplicates_booker_passport():
    maestro = Booker()
    name_list = []
    passports = []
    passengers = []
    for i in range(50):
        name_list.append(
            "".join(random.choice(string.ascii_lowercase) for _ in range(7))
        )
        passport_number = random.randint(1000, 10000)
        while passport_number in passports:
            passport_number = random.randint(1000, 10000)
        passports.append(passport_number)
        passengers.append(Passenger(name_list[i], passports[i]))
        maestro.reserve_ticket(passengers[i], True)
    assert checkIfDuplicates(maestro.passport_dtb) == False

