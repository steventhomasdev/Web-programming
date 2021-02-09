value = 'y'

class flights():
    def __init__(self,capacity):
        self.capacity = capacity
        self.list = [] 
    def Add_passengers(self,name):
        self.list.append(name)

    def open_seats(self):
        return self.capacity - len(self.list)

def passengers(name):
    if(flight.open_seats()):
        flight.Add_passengers(name)
        print(f"\n open seats : {flight.open_seats()}")
    else:
        print(f"\n {name} is not added due to unavailablity of seats")

def print_pass():
    print("\n No more seats available")
    print("\nplease see the current list of passengers in the flight\n")
    print(flight.list)
    

flight = flights(5)

while(value == 'y' or value == 'Y'):
    passengers(input('\n please enter the name: '))
    value = input("\n is there more names to add y/n: ")
    if(value != 'y' or value != 'Y'):
        print("\nplease see the current list of passengers in the flight\n")
        print(flight.list)
    if(not flight.open_seats()):
        print_pass()
        value = 'n'

