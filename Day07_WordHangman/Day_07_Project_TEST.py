import random
from logo import logo
from words import words
from stages import stages
import os

chosen_word = random.choice(words)

end_of_game = False
lives = 6

display = []

for i in range(len(chosen_word)):
    display.append("_")

print(display)

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    os.system('clear')

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            #display[pos] = guess

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("Letter is not in the word - you have lost a life.")
        print(f"Remaining word chances: {lives}")
        if lives == 0:
            end_of_game = True
            print("You LOST!")

    if "_" not in display:
        end_of_game = True
        print("You have won, yayyy!!!")

    print(stages[lives])