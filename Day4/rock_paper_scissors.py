import random

user_choice = int(input("type 0 for rock, 1 for paper, 2 for scissors:  "))

computer_choice = random.randint(0,2)
print(computer_choice)

if user_choice >= 3 or user_choice < 0:
    print("You entered a wrong number. You lose")
elif computer_choice == user_choice:
    print("Draw")
elif computer_choice== 0 and user_choice == 2:
    print("you loose")
elif computer_choice== 1 and user_choice == 0:
    print("You lose")
elif computer_choice == 2 and user_choice == 1:
    print("you lose")

else:
    print("You win")

