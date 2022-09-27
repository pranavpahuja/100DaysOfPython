import random
from logo import logo

def encode(word, shift):
    encoded = ""
    shift = int(shift)
    for i in range(0, len(word)):
        letter = word[i]
        charVal = int(ord(letter))
        charVal += shift
        encoded += chr(charVal)
    print(f"Encoded string is: {encoded}")

def decode(word, shift):
    decoded = ""
    shift = int(shift)
    for i in range(0, len(word)):
        letter = word[i]
        charVal = int(ord(letter))
        charVal -= shift
        decoded += chr(charVal)
    print(f"Decoded string is: {decoded}")

print(logo)

print("Type 'encode' to encrypt, type 'decode' to decrypt:")
choice = input(" ")

if choice == 'encode':
    word_v = input("Type your message: ")
    shift_v = input("Type the shift number: ")
    encode(word_v, shift_v)
elif choice == 'decode':
    word_v = input("Type encoded message: ")
    shift_v = input("Type the shift number: ")
    decode(word_v, shift_v)
else:
    print("Wrong Choice!!!")
