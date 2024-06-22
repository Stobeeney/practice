class Vehicle:
    def vehicle_info(self):
        print("inside vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("inside car class")


class Truck(Vehicle):
    def truck_info(self):
        print("inside truck class")


class SportsCar(Car):
    def SportsCar_info(self):
        print("inside sports car class")


s_car = SportsCar()
s_car.vehicle_info()
s_car.car_info()
s_car.SportsCar_info()
