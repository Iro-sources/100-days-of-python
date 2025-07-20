import pyfiglet

ascii_banner = pyfiglet.figlet_format("Pizza Delivery")
print(ascii_banner)

size = input("Choose size for pizza 'S', 'M' or 'L' ")
pepperoni = input("Do you want pepperoni? 'yes' or 'no'? ")
extra_cheese = input("Do you want extra cheese? 'yes' or 'no' ")

price = 0

if size == 'S':
    price = 15
elif size == 'M':
    price = 20
elif size == 'L':
    price = 25
else:
    print("You typed wrong letters")

    if pepperoni == 'yes' and size == 'S':
        price +=2
    else: price +=3

    if extra_cheese == 'yes':
        price += 1
    print(f"The total price is: ${price}")


