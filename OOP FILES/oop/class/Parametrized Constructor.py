class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print(self.name, self.age, self.salary)


wosie = Employee("Wosie", 12, 800000)
wosie.show()

pompom = Employee("PomPom", 14, 90000)
pompom.show()
