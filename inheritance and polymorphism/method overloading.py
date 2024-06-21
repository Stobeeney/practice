def addition(a, b):
    c = a + b
    print(c)


def addition(a, b, c):
    d = a + b + c
    print(d)


addition(3, 7, 5)


class shape:
    def area(self, a, b=0):
        if b > 0:
            print("The area of Rectangle is: ", a * b)

        else:
            print("Area of square is: ", a ** 2)


square = shape()
square.area(5)

rectangle = shape()
rectangle.area(5, 3)
