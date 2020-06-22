
file = open("test.txt", "w")

file.write('Hello World!')

file.close()

file = open("test.txt", "r")

r = file.read()
print(r)
file.close()
