from random import randint

#the bug
# def my_function():
#     for i in range(1, 20):
#         if i == 20: #20 but max range is 19
#             print("You got it.")
# my_function()

#reproducing the bug
def calcDice():
    diceImg = ["1", "2", "3", "4", "5", "6"]
    diceNum = randint(1, 6) #includes both 1 and 6.
    print(diceImg[diceNum])
calcDice()