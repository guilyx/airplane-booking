import random

class Booker():
    def __init__(self):
        super().__init__()
        self.destinations = ["New York", "Paris", "London", "Tokyo"]
        self.ticket_list = []
        self.data_base = dict()


    def generate_ticket(self, passenger):
        ticket = random.randint(1000, 100000)
        while(ticket in self.ticket_list):
            ticket = random.randint(1000, 100000)
        self.ticket_list.append(ticket)
        return ticket

    
    
