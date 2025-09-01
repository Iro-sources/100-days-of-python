alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to  decrypt:\n ").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: create function called 'encrypt()' that takes 'original_text and shift_amount as 2 inputs
def encrypt(original_text, shift_amount):
    # Use the shifted position to get the new letter from the alphabet list: alphabet[shifted_position].

    # Accumulate the shifted letters into a string called ciphertext. Initialize ciphertext as an empty string before the loop.

    # Inside the loop, append each shifted letter to ciphertext using ciphertext += new_letter.
    for letter in original_text:
        alphabet.index(letter)
        new_letter = letter
        cipher_text += new_letter
        shifted_letter = shift
        alphabet[shifted_letter]

    # After the loop completes, print the encoded result using an f-string: print(f"Here is the encoded result: {ciphertext}").
    cipher_text = " "
    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)

