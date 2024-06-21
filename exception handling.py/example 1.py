x = 2
y = 0

try:
    result = x // y
    print("Yeah! your answer is: ", result)

except ZeroDivisionError:
    print("Sorry! You are dividing by zero ")

finally:
    print("End of Program")
