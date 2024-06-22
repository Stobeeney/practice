class Student:
    school_name = "PUP"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("student: ", self.name, self.age, Student.school_name)

    def change_age(self, new_age):
        self.age = new_age

    @classmethod
    def modify_school_name(cls, new_name):
        cls.school_name = new_name


s1 = Student("bombom", 12)
s1.show()
s1.change_age(13)

Student.modify_school_name("PUP Main")

s1.show()
