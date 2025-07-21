import pyfiglet
ascii_banner = pyfiglet.figlet_format("Treasure Island")
print(ascii_banner)

choice1 = input("choose a direction: 'left' or 'right'? ").lower()

if choice1 == 'left':
    choice2 = input("choose action: 'swim' or 'wait'? ").lower()

    if choice2 == 'wait':
        choice3 = input("which door: 'blue' 'yellow' or 'red'? ").lower()
        if choice3 == 'red':
            print("You entered a room full of fire. Game over")
        elif choice3 == 'yellow':
            print("You found the treasure. You win")
        elif choice3 == 'blue':
            print("You entered a room of beast. Game over")
        else:
            print("You chose a wrong door. Game over")

    else:
        print("Game over")

else:
    print("Game over")
