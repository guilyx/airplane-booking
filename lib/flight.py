'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 02/02/2020
@brief : airplane reservation program
'''

from lib.passenger import Passenger
import random
from sys import stdout

class Flight():
    def __init__(self, destination):
        self.passenger_list = []
        self.max = random.randint(100, 350)
        self.destination = destination

    
    def add_passenger(self, Passenger):
        if (len(self.passenger_list) < self.max):
            self.passenger_list.append(Passenger)


    def remove_passenger(self, Passenger):
        for elem in self.passenger_list:
            if elem == Passenger:
                self.passenger_list.remove(Passenger)
            

    def print_passenger(self):
        i = 0
        for elem in self.passenger_list:
            stdout.write(elem.pseudo + " ; ")
            if i > 20:
                stdout.write('\n')
                i = 0
            i += 1