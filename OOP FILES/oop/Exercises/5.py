# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# aDefine a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


bus = Bus("School Honda", 180, 10)
print("Name: ", bus.name, "Color: ", bus.color, "Max speed: ",
      bus.max_speed, "Mileage: ", bus.mileage)

car = Car("Adventure", 150, 8)
print("Name: ", car.name, "Color: ", car.color, "Max speed: ",
      car.max_speed, "Mileage: ", car.mileage)
