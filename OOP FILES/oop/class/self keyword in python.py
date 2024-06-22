class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


daniel = Student("Daniel", 20)
daniel.show()

Phia = Student("Phia", 20)
Phia.show()
