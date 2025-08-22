allowed_char = input("Enter allowed characters: ")

# // Ask how many words the user wants to input
num_of_words = int(input("Enter amount of words: "))

# // Initialize an array of strings to store the user's words
list_of_words = []
#for word in range(1, num_of_words+1):
for i in range(num_of_words):
    word = input(f"Enter word {i+1}: ")
    list_of_words.append(word)

count = 0
for word in list_of_words:
    isConsistent = True
    for c in word:
        if c not  in allowed_char:
            isConsistent = False
            break
    if isConsistent:
        count += 1

print(count)
