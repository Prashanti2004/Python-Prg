#Hybrid Inheritence
class Vehicle:
    def description(self):
        print("This is a vehicle.")

class Engine:
    def engine_type(self):
        print("Engine type is disel")

class Car(Vehicle,Engine):
    def wheels(self):
        print("car has four wheels")

car = Car()
car.description()
car.engine_type()