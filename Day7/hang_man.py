import random
from Day7.hangman_words import word_list
from Day7.hangman_art import stages

STARTING_LIVES = 6


def choose_word(word_list):
    """Pick a random word from the list."""
    return random.choice(word_list)


def create_placeholder(word, guessed_letters):
    """Return the display string with guessed letters revealed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def play_hangman():
    chosen_word = choose_word(word_list)
    guessed_letters = set()
    lives = STARTING_LIVES
    game_over = False

    print("Welcome to Hangman!")
    print(create_placeholder(chosen_word, guessed_letters))

    while not game_over:
        guess = input("Guess a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print("✅ Good guess!")
        else:
            print(f"❌ '{guess}' is not in the word.")
            lives -= 1

        print(create_placeholder(chosen_word, guessed_letters))
        print(f"Lives left: {lives}")
        print(stages[lives])

        if "_" not in create_placeholder(chosen_word, guessed_letters):
            game_over = True
            print(f"🎉 You win! The word was '{chosen_word}'.")
        elif lives == 0:
            game_over = True
            print(f"💀 You lose! The word was '{chosen_word}'.")


if __name__ == "__main__":
    play_hangman()
