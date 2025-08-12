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

game_over = False
correct_letter = [ ]
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()
    display_letter = " "

    for letter in chosen_word:
        if guess == letter:
            display_letter += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display_letter += letter
        else:
            display_letter += "_ "
    print(display_letter)

    if guess not  in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose! ")

    if "_" not  in display_letter:
        game_over = True
        print("You win! ")
