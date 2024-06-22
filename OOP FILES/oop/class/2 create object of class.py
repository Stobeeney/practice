class Person:

    def __init__(self, name, sex, profession):

        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        print("name: ", self.name, "sex: ", self.sex,
              "profession: ", self.profession)

    def work(self):
        print(self.name, "working as a", self.profession)


Daniel = Person("Daniel", "Male", "Computer Enginner")

Daniel.show()
Daniel.work()
