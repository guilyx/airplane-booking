'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 02/02/2020
@brief : airplane reservation program
'''


import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from lib.passenger import Passenger
from lib.booker import Booker
from lib.flight import Flight

def check_ticket_number():
    booker = Booker()
    p1 = Passenger("Norbert", 101)
    booker.reserve_ticket(p1, True)
    assert(len(booker.ticket_list) == 1)
    