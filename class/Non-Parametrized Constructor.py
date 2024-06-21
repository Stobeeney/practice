class Company:
    def __init__(self):
        self.name = "Pynative"
        self.address = "ABC Street"

    def show(self):
        print('Name: ', self.name, "Address: ", self.address)


# Instantiate the Company class
cmp = Company()

# Call the show method
cmp.show()
