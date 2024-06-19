f = open("main.txt")
print(f.read())  # read the entire file
f.close()


f = open("main.txt")
print(f.read(5))  # read the first file
f.close()


f = open("main.txt")
print(f.readline())  # read the last line file
f.close()

f = open("main.txt")
data = f.readlines()
for line in data:
    print(line)
