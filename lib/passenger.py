'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 02/02/2020
@brief : airplane reservation program
'''

from os import system
class Passenger():
    def __init__(self, pseudo, passport_number):
        self.pseudo = pseudo
        self.passport_number = passport_number
        self.has_booked = False
        self.tickets = []
        self.book = dict()
        self.n_tickets = 0


    def book_ticket(self, Flight, ticket):
        self.book[Flight.destination] = ticket
        self.tickets.append(ticket)
        self.has_booked = True
        self.n_tickets += 1
    
    
    def remove_ticket(self, Flight, ticket):
        self.book.pop(Flight.destination)
        self.tickets.remove(ticket)
        self.n_tickets -= 1
        if (self.n_tickets == 0):
            self.has_booked = False


    def print_info(self):
        system('clear')
        print("\n\r")
        print("---- PASSENGER INFORMATION ----")
        print("- Name : " + self.pseudo)
        print("- Passeport Number : " + str(self.passport_number))
        if (self.n_tickets == 0):
            print("- No plane ticket(s) found...")
        else:
            self.print_tickets()
        

    def print_tickets(self):
        print("\n\r")
        print("---- TICKET(S) HELD ----")
        print(self.pseudo + " holds " + str(self.n_tickets) + " ticket(s).")
        print(self.book)
        