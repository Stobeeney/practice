# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


bus = Bus("School Bus", 40, 60)
print("vehicle name: ", bus.name, "max speed is: ",
      bus.max_speed, "mileage is: ", bus.mileage)
