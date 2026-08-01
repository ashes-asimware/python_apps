class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def open_trunk(self):
        return "Trunk opened"

class Motorcycle(Vehicle):
    def pop_wheelie(self):
        return "Popped a wheelie!"
    
class Truck(Vehicle):
    def haul_cargo(self):
        return "Hauling cargo"
    
car = Car("Toyota", "Camry")
print(car.start_engine())
print(car.open_trunk())

motorcycle = Motorcycle("Harley-Davidson", "Street 750")
print(motorcycle.start_engine())
print(motorcycle.pop_wheelie())

truck = Truck("Ford", "F-150")
print(truck.start_engine())
print(truck.haul_cargo())

