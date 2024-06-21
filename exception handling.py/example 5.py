try:
    f = open("demo.txt", "w")
    f.write("BWAHSHAHSHASHA")
    print("Something went wrong in the file")
finally:
    f.close()
