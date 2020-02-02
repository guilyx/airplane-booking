'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 02/02/2020
@brief : airplane reservation program
'''

class Passenger():
    def __init__(self, pseudo, passeport_number):
        self.pseudo = pseudo
        self.passeport_number = passeport_number
        self.has_booked = False
        self.n_tickets = 0

    def print_info(self):
        print("---- PASSENGER INFORMATION ----")
        print("- Name : " + self.pseudo)
        print("- Passeport Number : " + self.passeport_number)
        if (self.n_tickets == 0):
            print("- No plane tickets found...")
        else:
            print("- " + self.n_tickets + " tickets booked !")

    def print_tickets(self):
        print("---- TICKETS HELD ----")
        print(self.pseudo + " holds " + self.n_tickets + " tickets.")
        # print destinations, tickets number etc

    def book(self):
        pass
        