import random

from reportlab.lib.pagesizes import letter

word_list = ["aardvark", "baboon", "camel"]

chosen_word= random.choice(word_list)
print(chosen_word)

place_holder = " "

word_length = len(chosen_word)
for position in range(word_length):
    place_holder += "_ "

print(place_holder)

display_letter = " "
guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if guess == letter:
        display_letter += letter
    else:
        display_letter += "_ "
print(display_letter)
