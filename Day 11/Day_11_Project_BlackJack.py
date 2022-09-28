import random

all_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5,
             6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

my_score = 0
my_cards = []
computer_score = 0
computer_card = []

def calcScore(cards_list):
    """Calculates score by reading a cards list."""
    score = 0
    for card in cards_list:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            score += 1
        else:
            score += int(card)
    return score

def result(bot_score_fin, my_score_fin):
    if bot_score_fin > 21:
        print("Bot has cards > 21. You WIN!")
        return True
    elif my_score_fin > 21:
        print("You have cards > 21. Bot WINS!")
        return True
    else:
        if bot_score_fin > my_score_fin:
            print(f"Your Cards: {my_cards}")
            print(f"Your Score: {my_score_fin}")
            print(f"Computer's Cards: {computer_card}")
            print(f"Computer's Score: {bot_score_fin}")
            print("Well, you LOST! The bot wins!")
        elif bot_score_fin == my_score_fin:
            print(f"Your Cards: {my_cards}")
            print(f"Your Score: {my_score_fin}")
            print(f"Computer's Cards: {computer_card}")
            print(f"Computer's Score: {bot_score_fin}")
            print("Well, it's a DRAW!")
        elif bot_score_fin < my_score_fin:
            print(f"Your Cards: {my_cards}")
            print(f"Your Score: {my_score_fin}")
            print(f"Computer's Cards: {computer_card}")
            print(f"Computer's Score: {bot_score_fin}")
            print("Well, you WON! The bot lost.")
        return False
def botTurn():
    card = random.choice(cards)

    computer_card.append(card)

    return calcScore(computer_card)

def assignPlayerACard():

    card = random.choice(cards)

    my_cards.append(card)

    return calcScore(my_cards)

def setup():

    card1 = random.choice(cards)
    card2 = random.choice(cards)
    card3 = random.choice(cards)

    my_cards.append(card1)
    my_cards.append(card2)
    my_score = calcScore(my_cards)

    computer_card.append(card3)
    computer_score = calcScore(computer_card)

    print(f"Cards: {my_cards}")
    print(f"Score: {my_score}")

    print(f"Cards: {computer_card}")
    print(f"Score: {computer_score}")

def runOrNot(getChoice):

    if getChoice == 'n':
        bot_score_fin = botTurn()
        my_score_fin = calcScore(my_cards)
        result(bot_score_fin, my_score_fin)

    elif getChoice == 'y':

        print("____________________________________")
        my_score = assignPlayerACard()
        print(f"Your Cards: {my_cards}")
        print(f"Your Score: {my_score}")

        computer_score = calcScore(computer_card)
        print(f"Computer's Cards: {computer_card}")
        print(f"Computer's Score: {computer_score}")

        print("Bot is thinking ...")

        computer_score = botTurn()

        print(f"Your Cards: {my_cards}")
        print(f"Your Score: {my_score}")

        print(f"Computer's Cards: {computer_card}")
        print(f"Computer's Score:: {computer_score}")

        print("____________________________________")

        if not result(computer_score, my_score):
            choice_f = 'y'
            runOrNot(choice_f)

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if start == 'y':
    setup()
    choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    runOrNot(choice)