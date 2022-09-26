import random
rock = '''
    _________
---'   ______)
      (________)
      (_______)
      (______)
---.__(____-)
'''

paper = '''
    _________
---'   ______)____
          ________)
          _________)
         _________)
---.____________)
'''

scissors = '''
    _______
---'   ____)______
          ________)
       ____________)
      (____)
---.__(___)
'''

turn = int(input("What do you choose? Rock (1), Paper (2) or Scissors (3) ?"))

list1 = [1, 2, 3]
bot = random.choice(list1)

if turn == 1:
    print("You chose ROCK: \n"+rock)
elif turn == 2:
    print("You chose PAPER: \n"+paper)
if turn == 3:
    print("You chose SCISSORS: \n" + scissors)
else:
    print("Wrong Choice!")

if bot == 1:
    print("The bot chose ROCK: \n"+rock)
elif bot == 2:
    print("The bot chose PAPER: \n"+paper)
if bot == 3:
    print("The bot chose SCISSORS: \n" + scissors)

win = 0

if turn == 1 and bot == 2:
    win = 0
elif turn == 1 and bot == 3:
    win = 1
elif turn == 2 and bot == 1:
    win = 1
elif turn == 2 and bot == 3:
    win = 0
elif turn == 3 and bot == 1:
    win = 0
elif turn == 3 and bot == 2:
    win = 1
elif turn == bot:
    win = 2

if win == 1:
    print("You have won!")
elif win == 2:
    print("Ah, it's a draw.")
elif win == 0:
    print("Oops. You've lost!")