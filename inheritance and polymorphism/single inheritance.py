class vehicle:
    def Vehicle_info(self):
        print("Inside Vehicle Class")


class Car(vehicle):
    def car_info(self):
        print("Insifr Car Class")


car = Car()

car.Vehicle_info()
car.car_info()
