import random

NUMBER = random.randint(1,101)

LIVES = 0

ISOVER = False

def setup():

    global LIVES

    lives_dict = {"1":10,"2":7,"3":5,"4":3}

    print('''/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/
/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/
Welcome to the NUMBER GUESSER game.
Here are the difficulty settings:
'1' for Amateur: "I'm a noob, keep it easy"
'2' for Familiar: "I know what this is. Let me try.
'3' for Experienced: "I have played many times - let me show my skill.
'4' for Pro: "I am a king - throw me any challenge, and I'll win it."''')

    difficulty = input("Choose a difficulty for the game: ").lower()

    LIVES = lives_dict[difficulty]

    print(LIVES)

    print(f"Pssstt.. number is {NUMBER}")

setup()

while not ISOVER and LIVES > 0:

    number = NUMBER



    guess = int(input("Guess the number?! : "))

    if guess == number:

        print(f"Damn nice, you have won! {number} is the number, indeed.")
        if LIVES == 1:
            print("You had only 1 life left, phew.")
        else:
            print(f"You had {LIVES} lives left.")
        ISOVER = True

    elif guess > number:

        print("Your guess is bigger than the number.")
        LIVES -= 1
        print(f"You have {LIVES} lives left.")

    elif guess < number:

        print("Your guess is lesser than the number.")
        LIVES -= 1
        print(f"You have {LIVES} lives left.")