age = 3
if age < 0:
    raise Exception("Sorry, age is out of range")

age = "30"
if type(age) is int:
    raise Exception("Sorry, age is out of range")
