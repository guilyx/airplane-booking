import random
import os
from lib.flight import Flight
from lib.passenger import Passenger
import time


class Booker():
    def __init__(self, destinations_list = None):
        if destinations_list == None:
            self.destinations = ["New York", "Paris", "London", "Tokyo"]
        else: 
            self.destinations = destinations_list
        self.flight_dtb = dict()

        i = 0
        for elem in self.destinations:
            self.flight_dtb[elem] = Flight(elem)
            i += 1

        self.passport_dtb = []
        self.passenger_dtb = dict()
        self.ticket_list = []

        self.exit = False

    
    def main_menu(self):
        self.exit = False
        os.system('clear')
        print("---- MENU ----")
        known = False
        name = input("Enter your name ---- ")
        pass_n = input("Enter your passport number ---- ")
        for items, keys in self.passenger_dtb.items():
            if pass_n in items:
                known = True
            else:
                known = False
        if not(known):
            self.passenger_dtb[pass_n] = Passenger(name, pass_n)
        else:
            print("Oh, you're already registered !")
        self.current_user = self.passenger_dtb[pass_n]
        print("Hello " + name + " what do you want to do ?\n 1 - Reserve a Ticket\n 2 - Cancel a reservation\n 3 - Display ticket information.\n 4 - Exit")
        opt = int(input("Choice ---- "))
        
        if(opt == 1):
            self.reserve_ticket(self.current_user)
        elif(opt == 3):
            self.display_info(self.current_user)
        elif(opt == 4):
            self.exit = True
        else:
            print("Not yet implemented.")


    
    def reserve_ticket(self, Passenger, rand_dest = False):
        if (rand_dest == False):
            os.system('clear')
        print("---- MENU ----")
        for i in range(len(self.destinations)):
            print(str(i + 1) + " : " + self.destinations[i])
        if rand_dest == False:
            dest = 0
            while dest < 1 or dest > len(self.destinations):
                dest = int(input("Choice : "))
        else:
            dest = random.randint(1, len(self.destinations))

        chosen_flight = self.flight_dtb[self.destinations[dest - 1]]
        
        if(Passenger.passport_number in self.passport_dtb):
            print("Your Passport Number is already used by someone, are you sure it is correct ?")
        else:
            self.passport_dtb.append(Passenger.passport_number)
        ticket = self.generate_ticket(Passenger)
        Passenger.book_ticket(chosen_flight, ticket)
        chosen_flight.add_passenger(Passenger)
        print("Your ticket for " + chosen_flight.destination + " has been successfully booked.")
        print("Returning to main menu...")
        if not(rand_dest):
            input("Press Enter to continue...")
            time.sleep(2)

        
    def cancel_ticket(self, Passenger, rand_dest = False):
        pass
        '''if (rand_dest == False):
            os.system('clear')
        print("---- MENU ----")
        Passenger.print_tickets()
        if rand_dest == False:
            dest = 0
            while dest < 1 or dest > len(self.destinations):
                dest = int(input("Choice : "))
        else:
            dest = random.randint(1, len(self.destinations))

        chosen_flight = self.flight_dtb[self.destinations[dest - 1]]
        
        if(Passenger.passport_number in self.passport_dtb):
            print("Your Passport Number is already used by someone, are you sure it is correct ?")
        else:
            self.passport_dtb.append(Passenger.passport_number)
        ticket = self.generate_ticket(Passenger)
        Passenger.book_ticket(chosen_flight, ticket)
        chosen_flight.add_passenger(Passenger)
        print("Your ticket for " + chosen_flight.destination + " has been successfully booked.")
        print("Returning to main menu...")
        if not(rand_dest):
            input("Press Enter to continue...")
            time.sleep(2)'''


    def display_info(self, Passenger):
        Passenger.print_info()
        input("Press Enter to continue...")
        

    def generate_ticket(self, Passenger):
        ticket = random.randint(1000, 100000)
        while(ticket in self.ticket_list):
            ticket = random.randint(1000, 100000)
        self.ticket_list.append(ticket)
        return ticket

    
    
