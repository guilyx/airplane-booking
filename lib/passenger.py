'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 02/02/2020
@brief : airplane reservation program
'''

from os import system
class Passenger():
    def __init__(self, pseudo, passeport_number):
        self.pseudo = pseudo
        self.passeport_number = passeport_number
        self.has_booked = False
        self.tickets = []
        self.book = dict()
        self.n_tickets = 0


    def book_ticket(self, Flight, ticket):
        self.book[Flight.destination] = ticket
        self.tickets.append(ticket)
        self.has_booked = True
        self.n_tickets += 1
    

    def print_info(self):
        system('clear')
        print("\n\r")
        print("---- PASSENGER INFORMATION ----")
        print("- Name : " + self.pseudo)
        print("- Passeport Number : " + str(self.passeport_number))
        if (self.n_tickets == 0):
            print("- No plane tickets found...")
        else:
            self.print_tickets()
        

    def print_tickets(self):
        print("\n\r")
        print("---- TICKETS HELD ----")
        print(self.pseudo + " holds " + str(self.n_tickets) + " tickets.")
        print(self.book)
        