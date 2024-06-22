class student:
    def __init__(self, name, age=12, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    def show(self):
        print(self.name, self.age, self.classroom)


wosie = student("Wosie")
wosie.show()

leamfey = student("leamfy", 14)
leamfey.show()

cweam = student("cweam", 14)
cweam.show()
