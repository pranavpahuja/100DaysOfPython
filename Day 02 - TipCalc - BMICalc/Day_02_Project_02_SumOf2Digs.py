number = input("Enter a 2 digit number: ")

number_i = int(number)

if number_i > 99 or number_i < 10:
    print("This is not a 2 digit number! Calculating for 1st 2 digits...")

sum = int(number[0]) + int(number[1])

print("The sum of the 2 digits is: {}".format(sum))