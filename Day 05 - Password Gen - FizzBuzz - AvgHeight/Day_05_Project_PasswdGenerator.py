import random

print("Welcome to the Password Generator!")

length = int(input("How many letters would you like in the password?"))
syms = int(input("How many symbols would you like?"))
nums = int(input("How many numbers would you like?"))

total_len = length+syms+nums
print("Total password length: {}".format(total_len))

password = ""

for i in range(total_len):
    x = random.randint(0,2)
    if x == 0:
        y = random.randint(0,1)
        if y == 0:
            char2 = random.randint(65,90)
            password += chr(char2)
        elif y == 1:
            char2 = random.randint(97, 122)
            password += chr(char2)
    elif x == 1:
        char1 = random.randint(33, 45)
        password += chr(char1)
    elif x == 2:
        char3 = random.randint(48, 57)
        password += str(char3)

print(f"Here's the generated password: {password}")