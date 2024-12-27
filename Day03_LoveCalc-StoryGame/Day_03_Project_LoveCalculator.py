print("Welcome to the love calculator!")
name1 = input("What is your name?").upper()
name2 = input("What is their name?").upper()

counter1 = 0
counter2 = 0

for char in name1+name2:
    for char2 in "TRUE":
        if char == char2:
            counter1 += 1
    for char3 in "LOVE":
        if char == char3:
            counter2 += 1

net_score = int(str(counter1)+str(counter2))

if net_score <10 or net_score>90:
    print(f"Your score is {net_score}, you go together like coke and mentos.")
elif net_score <50 and net_score>40:
    print(f"Your score is {net_score}, you're alright together.")
else:
    print(f"Your score is {net_score}.)