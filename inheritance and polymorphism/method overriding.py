class Vehicle:
    def max_speed(self):
        print("Max speed is 100 Km/Hour")


class Car(Vehicle):
    def max_speed(self):
        print("Max speed is 200 Km/Hour")


car = Car()
car.max_speed()
