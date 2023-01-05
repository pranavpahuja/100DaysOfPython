import pandas as pd

phonetic_data = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in phonetic_data.iterrows()}

name = input("Enter a word: ").upper()
letters_list = [new_dict[letter] for letter in name]

print(letters_list)

