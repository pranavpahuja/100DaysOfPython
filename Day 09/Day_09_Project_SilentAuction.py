import random

print("Welcome to secret auction program!")

bid_register = {'':''}

def showMax():

    keyMax = max(zip(bid_register.values(), bid_register.keys()))[1]

    print(f"Bid Winner : {keyMax}. Bid Money: {bid_register[keyMax]}")

def addToList(name, bid):

    bid_register[name] = bid

def getDetails():

    name = input("What is your name?")

    bid = input("What's your bid?")

    addToList(name, bid)

    answer = input("Are there any other bidders?").lower()

    if answer == 'yes':
        getDetails()
    elif answer == 'no':
        print("Bid Info saved ...")
        showMax()
    else:
        print("Wrong choice!")

getDetails()