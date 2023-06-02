class Human:
    def __init__(self, name='Human'):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def

    def add_passenger(self, *humans):
        self.passengers +=human

    def print_passengers(self):
        if self.passengers:
            print(f'Names of passengers in {self.brand}:')
            for p in self.passengers:
                print(p.name)
        else:
            print(f'There are no passengers in {self.brand}:')


nick = Human('Nick')
kate = Human('Kate')
andrew = Human('Andrew')
car = Auto('BMW')
car.add_passengers(nick, kate, andrew)
car.print_passengers()


