print("Welcome to the Tip Calculator!")

total_amount = float(input("What was your total bill amount?"))

no_of_people = float(input("How many people to split the bill amongst?"))

tip_perc = float(input("How much % tip do you want to give?"))

total_amt_inc_tip = total_amount + (total_amount*(tip_perc/100))

each_amount = total_amt_inc_tip/no_of_people

print("Each share comes to about: ${} - thanks for using the service!".format(each_amount))