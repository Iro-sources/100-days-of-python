#Multiple if statements
# height = float(input("Enter your height: "))
# if height >= 120:
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         photo = input("Do you want photo? 'yes' or 'no'")
#         if photo == 'yes':
#             print("The ticket is $15")
#         else: print("The ticket is 12")
#     elif age >= 12:
#         photo = input("Do you want photo? 'yes' or 'no'")
#         if photo == 'yes':
#             print("The ticket is $10")
#         else:
#             print("The ticket is 7")
#     elif age < 12:
#         photo = input("Do you want photo? 'yes' or 'no'")
#         if photo == 'yes':
#             print("The ticket is $8")
#         else:
#             print("The ticket is 5")
#
# else: print("You are too young to ride")

#Version two for better
#Ask the photo question once, after age and height checks.
height = float(input("Enter your height: "))
price = 0
if height >= 120:
    age = int(input("Enter your age: "))
    if age >= 18:
        price = 12
    elif age >= 12:
        price = 7
    else:
        price = 5
    photo = input("Do you want photo? 'yes' or 'no' ")
    if photo.strip().lower() == 'yes':
        price += 3
        print(f"Your total ticket cost is ${price}. Enjoy your ride!")
    else: print(f"Your total ticket cost is ${price}. Enjoy your ride!")
else: print("You are too young to ride")