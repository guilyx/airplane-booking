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

        self.current_user = None
        self.main_menu_it = 0

        self.exit = False

    
    def main_menu(self):
        self.exit = False
        os.system('clear')
        print("---- MENU ----")
        known = False
        same_user = False
        if self.main_menu_it > 0:
            choice = input("Are you still " + self.current_user.pseudo + "---- y/n")
            if (choice == 'y'):
                pass_n = input("Enter your passport number ---- ")
                if(pass_n == self.current_user.passport_number):
                    print("Welcome back !")
                    same_user = True
                else:
                    print("Your passport number didn't correspond ! Resetting the menu.")
                    same_user = False

        if (not(same_user)):
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

        print("Hello " + self.current_user.pseudo + " what do you want to do ?\n 1 - Reserve a Ticket\n 2 - Cancel a reservation\n 3 - Display ticket information.\n 4 - Exit")
        opt = int(input("Choice ---- "))
        
        if(opt == 1):
            self.reserve_ticket(self.current_user)
        elif(opt == 2):
            self.cancel_ticket(self.current_user)
        elif(opt == 3):
            self.display_info(self.current_user)
        elif(opt == 4):
            self.exit = True
        else:
            print("Not yet implemented.")
        self.main_menu_it += 1

    
    def reserve_ticket(self, Passenger, auto_test = False):
        if (auto_test == False):
            os.system('clear')
        print("---- MENU ----")
        for i in range(len(self.destinations)):
            print(str(i + 1) + " : " + self.destinations[i])
        if auto_test == False:
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
        if not(auto_test):
            input("Press Enter to continue...")
            time.sleep(2)

        
    def cancel_ticket(self, Passenger, auto_test = False):
        if (not(Passenger.has_booked)):
            print("You can't cancel tickets because you never booked one !")
            if (not(auto_test)):
                input("Press Enter to continue...")
        else:
            if (auto_test == False):
                os.system('clear')
            print("---- MENU ----")
            Passenger.print_tickets()
            cities, ticket_numb = list(Passenger.book.items())
            if (not(auto_test)):
                print(ticket_numb)
                selected_ticket = int(input("Type the ticket number you want to cancel."))
                while selected_ticket not in ticket_numb:
                    print("Ticket not found, type it again !")
                    selected_ticket = int(input("Type the ticket number you want to cancel."))
            else:
                selected_ticket = random.choice(ticket_numb)
                index = ticket_numb.index(selected_ticket)
                chosen_flight = self.flight_dtb[cities[index]]
            '''else:
                print("You only hold one ticket, removing " + str(Passenger.book))
                time.sleep(1)
                selected_ticket = Passenger.tickets[0]
                key = list(Passenger.book.keys())
                chosen_flight = self.flight_dtb[key[0]]'''

            Passenger.remove_ticket(chosen_flight, selected_ticket)
            self.ticket_list.remove(selected_ticket)
            chosen_flight.remove_passenger(Passenger)
            print("Your ticket for " + chosen_flight.destination + " has been successfully canceled.")
            print("Returning to main menu...")
            if not(auto_test):
                input("Press Enter to continue...")
                time.sleep(1)


    def display_info(self, Passenger):
        Passenger.print_info()
        input("Press Enter to continue...")
        time.sleep(2)
        

    def generate_ticket(self, Passenger):
        ticket = random.randint(1000, 100000)
        while(ticket in self.ticket_list):
            ticket = random.randint(1000, 100000)
        self.ticket_list.append(ticket)
        return ticket

    
    
