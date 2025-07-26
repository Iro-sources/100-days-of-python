import random

# Step 1: Start
def hangman():
    # Step 2: Generate a random word
    word_list = ["python", "hangman", "challenge", "developer", "function"]
    word = random.choice(word_list)
    word_letters = list(word)

    # Step 3: Generate as many blanks as letters in word
    blanks = ["_"] * len(word)
    lives = 6

    print("Welcome to Hangman!")
    print(" ".join(blanks))

    # Game loop
    while True:
        # Step 4: Ask the user to guess a letter
        guess = input("Guess a letter: ").lower()

        # Step 5: Is the guessed letter in the word?
        if guess in word_letters:
            # Step 6: Replace the blank with the letter
            for i in range(len(word_letters)):
                if word_letters[i] == guess:
                    blanks[i] = guess
            print("Correct!")
        else:
            # Step 7: Lose a life
            lives -= 1
            print(f"Wrong! Lives left: {lives}")

        # Display current state
        print(" ".join(blanks))

        # Step 8: Are all the blanks filled?
        if "_" not in blanks:
            print("Congratulations! You guessed the word.")
            break

        # Step 9: Have they run out of lives?
        if lives == 0:
            print(f"You've run out of lives. The word was '{word}'.")
            break

    # Step 10: Game over
    print("GAME OVER")

# Run the game
hangman()
