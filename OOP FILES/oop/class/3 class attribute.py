class Student:
    school_name = "PUP"
    # class variable

    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age


student_1 = Student("Tobee", 12)
# Access instance variable
print("Student: ", student_1.name, student_1.age)

# Acces instance variable
print("School name: ", Student.school_name)

# modify insantce variable
student_1.name = "owamge"
student_1.age = 14
print("Student: ", student_1.name, student_1.age)

# modify class variables
Student.school_name = "PUP MAIN"
print("School name: ", Student.school_name)
