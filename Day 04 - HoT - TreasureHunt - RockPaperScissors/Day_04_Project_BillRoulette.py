import random

print("Hello, welcome to the Bill Roulette!")

stringNames = input("Enter the string of names separated by a ',' like Sam,Peach,Jacob etc..:: ")

listOfNames = stringNames.split(",")

print(listOfNames)

random_int = random.randint(0, len(listOfNames))

print(f"Well, {listOfNames[random_int]} will have to pay the bill today!!")