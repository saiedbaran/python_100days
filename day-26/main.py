import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

npa = {row.letter: row.code for (index, row) in data.iterrows()}

print(npa)

user_input = input("Please Enter your text: ")
phonetic_list = [npa[f"{letter.upper()}"] for letter in user_input.lower() if letter.upper() in npa.keys()]

print(phonetic_list)
