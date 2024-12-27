print("Welcome to the HappyPizzaPlace!")

size = input("What size pizza do you want today? S, M or L ?")

pepperoni = input("Do you want pepperoni on it? Answer Y or N")

extra_cheese = input("Do you want extra cheese? Answer Y or N")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    elif size == 'M' or size == 'L':
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"The total bill amount is: {bill}.")