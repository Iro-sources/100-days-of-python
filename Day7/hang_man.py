import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word= random.choice(word_list)
print(chosen_word)

place_holder = " "

word_length = len(chosen_word)
for position in range(word_length):
    place_holder += "_ "

print(place_holder)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")

