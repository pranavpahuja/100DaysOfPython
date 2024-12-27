#score needs fixing

from art import logo
from art import vs
from game_data import data
import random

SCORE = 0

HASLOST = False

STARTINGVALUE = data[3]


def printDetails(startingVS):

    global STARTINGVALUE
    global HASLOST
    global SCORE

    score = SCORE

    A = startingVS["follower_count"]
    name = startingVS["name"]
    desc = startingVS["description"]
    cnt = startingVS["country"]

    print(f"Compare A: {name}, a {desc}, from {cnt}.")

    secondVS = random.choice(data)
    B = secondVS["follower_count"]
    name2 = secondVS["name"]
    desc2 = secondVS["description"]
    cnt2 = secondVS["country"]

    print(vs)

    print(f"Against B: {name2}, a {desc2}, from {cnt2}.")

    AminusB = int(A) - int(B)

    choice = input("Choose either 'A' or 'B': ")

    if choice == "A" and AminusB >=0:
        print("You're right!")
        printDetails(secondVS)
        SCORE += 1
    elif choice == "B" and AminusB <0:
        print("You're right!")
        printDetails(secondVS)
        SCORE += 1
    else:
        print("You're wrong!")
        HASLOST = True
        print(f"Your score is {SCORE}")

def setupGame():

    global STARTINGVALUE
    print(logo)
    printDetails(STARTINGVALUE)

while not HASLOST:
    setupGame()
