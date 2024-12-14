class Car:
    def __init__(self,brand,fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def car_details(self,milage: float):
        print(f"This is {self.brand} car and is {self.fuel_type} car and has a millage of {milage} kmph")

car1=Car(brand= "Benz", fuel_type="Disel")
car2=Car(brand="Porsche",fuel_type="Petrol")

car1.car_details(16)
car2.car_details(8)