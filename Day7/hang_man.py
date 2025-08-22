import random
from Day7.hangman_words import word_list
from Day7.hangman_art import stages

# In Python, constants are just uppercase variables by convention.
# In Java → use: final int STARTING_LIVES = 6;
# In C#   → use: const int STARTING_LIVES = 6;
STARTING_LIVES = 6


def choose_word(word_list):
    """
    Pick a random word from the list.
    Python: random.choice(list)
    Java:   list.get(rand.nextInt(list.size()))
    C#:     list[rand.Next(list.Count)]
    """
    return random.choice(word_list)


def create_placeholder(word, guessed_letters):
    """
    Return the display string with guessed letters revealed.
    Python: Uses list comprehension and " ".join([...])
    Java:   Use a StringBuilder, loop through each char in word,
            append either the letter or "_" and a space.
    C#:     Same as Java, using StringBuilder or simple string concatenation.
    """
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def play_hangman():
    """
    Main game logic loop.
    In Python, we write this as a free function.
    In Java/C#, this would be a static method inside a class,
    and called from the main() method.
    """
    chosen_word = choose_word(word_list)

    # Python: set() stores unique guessed letters (fast lookups, no duplicates)
    # Java:   Use HashSet<Character>
    # C#:     Use HashSet<char>
    guessed_letters = set()
    lives = STARTING_LIVES
    game_over = False

    print("Welcome to Hangman!")
    print(create_placeholder(chosen_word, guessed_letters))

    while not game_over:
        # Python: input() reads string from user
        # Java:   new Scanner(System.in).nextLine()
        # C#:     Console.ReadLine()
        guess = input("Guess a letter: ").lower().strip()

        # Validate input → must be 1 alphabetic character
        # Python: .isalpha(), len() check
        # Java:   Character.isLetter(guess.charAt(0)) && guess.length() == 1
        # C#:     char.IsLetter(guess[0]) && guess.Length == 1
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please guess a single letter.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        # Correct or wrong guess
        if guess in chosen_word:
            print("✅ Good guess!")
        else:
            print(f"❌ '{guess}' is not in the word.")
            lives -= 1

        # Show current word state
        print(create_placeholder(chosen_word, guessed_letters))

        # Lives counter
        print(f"Lives left: {lives}")
        # Python: list index stages[lives]
        # Java:   stages[lives] if stages is an array
        # C#:     stages[lives] if stages is a list or array
        print(stages[lives])

        # Win condition
        if "_" not in create_placeholder(chosen_word, guessed_letters):
            game_over = True
            print(f"🎉 You win! The word was '{chosen_word}'.")
        # Lose condition
        elif lives == 0:
            game_over = True
            print(f"💀 You lose! The word was '{chosen_word}'.")


# Python: This special check ensures code only runs when file is executed directly
# Java:   Just put game loop inside main() method
# C#:     Same as Java, inside static void Main()
if __name__ == "__main__":
    play_hangman()
