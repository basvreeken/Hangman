# Write your code here
from random import choice
print("H A N G M A N")
wordlist = ['python', 'java', 'kotlin', 'javascript']
chosen_word = choice(wordlist)
hint = chosen_word[0:3]
num_of_dashes = len(chosen_word) - 3
i = 0
while i != num_of_dashes:
    hint = hint + "-"
    i += 1

word = input(f"Guess the word: {hint}")

if word == chosen_word:
    print("You survived!")
else:
    print("You lost!")

