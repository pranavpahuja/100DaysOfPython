import random

def isPrime(number):

    count = 0

    for i in range(1,number+1):
        if number % i == 0:
            count += 1

    if count == 2 or number == 1:
        print(f"Number {number} is PRIME.")
    else:
        print(f"Number {number} is NOT PRIME.")

num = int(input("Check this number: "))
isPrime(num)