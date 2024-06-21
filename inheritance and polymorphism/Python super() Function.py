class Company:
    def company_name(self):
        return "Google"


class employee(Company):
    def info(self):
        c_name = super().company_name()
        print("Bumbum works at", c_name)


emp = employee()
emp.info()
