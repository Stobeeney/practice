# try
try:
    type = input("enter 'Hello World: ")
    print(type)
except Exception as e:
    print("An error occured")
else:
    print("No error")
finally:
    print("finished")
