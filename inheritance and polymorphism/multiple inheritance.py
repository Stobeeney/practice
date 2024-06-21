class Person:
    def person_info(self, name, age):
        print("Inside person class")
        print("Name: ", "Age: ", age)


class Company:
    def company_info(self, company_name, location):
        print("Inside company class")
        print("Name: ", company_name, "Location: ", location)


class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print("inside employee class")
        print("Salary:", salary, "Skills: ", skill)


emp = Employee()

emp.person_info("Piya", 20)
emp.company_info("AWS", "Philippines")
emp.Employee_info("89000", "Web Dev")
