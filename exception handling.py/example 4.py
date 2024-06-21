try:
    x = int(input("Enter the value of X: "))
    y = int(input("Enter the value of Y: "))

    result = x / y
    print(" Answer: ", result)

except ZeroDivisionError:
    print("Sorry! You are dividing by zero")

except ValueError:
    print("Sorry, wrong input. ")

finally:
    print("End of program.")
