import random
import os
from lib.flight import Flight
from lib.passenger import Passenger


class Booker():
    def __init__(self):
        super().__init__()
        self.destinations = ["New York", "Paris", "London", "Tokyo"]
        self.flight_dtb = dict()

        i = 0
        for elem in self.destinations:
            self.flight_dtb[elem] = Flight(elem)
            i += 1

        self.passenger_dtb = dict()

        self.ticket_list = []

    
    def main_menu(self):
        os.system('clear')
        print("---- MENU ----")
        print("Hello, what do you want to do ?\n 1 - Reserve a Ticket\n 2 - Cancel a reservation\n 3 - Display ticket information.\n 4 - Exit")
        opt = int(input("Choice ---- "))
        return(opt)

    
    def reserve_ticket(self, Passenger):
        os.system('clear')
        print("---- MENU ----")
        print("Which destination ?\n 1 : New York\n 2 : Paris\n 3 : London\n 4 : Tokyo")
        dest = 0
        while dest < 1 or dest > 4:
            dest = int(input("Choice : "))

        chosen_flight = self.flight_dtb[self.destinations[dest - 1]]
        ticket = self.generate_ticket(Passenger)
        Passenger.book_ticket(chosen_flight, ticket)
        chosen_flight.add_passenger(Passenger)


    def generate_ticket(self, Passenger):
        ticket = random.randint(1000, 100000)
        while(ticket in self.ticket_list):
            ticket = random.randint(1000, 100000)
        self.ticket_list.append(ticket)
        self.passenger_dtb[ticket] = Passenger.pseudo
        return ticket

    
    
