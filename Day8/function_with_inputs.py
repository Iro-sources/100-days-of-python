def greet():
    print("Hello")
    print("Good morning")
    print("Good night")

greet()


def life_in_weeks(age):
    result = 90 - age
    print(result * 52)


life_in_weeks(20)

def check_true_letters(name1, name2):
    combined_name = name1 + name2
    word1 = "TRUE"
    word2 = "LOVE"

    true_count = 0
    for letter in combined_name.upper():
        if letter in word1:
            true_count += 1


    love_count = 0
    for letter in combined_name.upper():
        if letter in word2:
            love_count += 1


    print (str(true_count) + str(love_count))



check_true_letters("mohamed", "qureysha")


