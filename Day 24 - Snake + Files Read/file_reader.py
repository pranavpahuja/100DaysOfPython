file = open("file.txt")
contents = file.read()
print(contents)

with open("file.txt", mode="a") as file:
    file.write("\nNew Line, hello!")
