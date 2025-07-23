print("New lines can be created with a \ and the letter n \n like this")

print("A tab can be created with a \ and the letter t \t like this")

#Switching variables
glass1 = "milk"
glass2 = "juice"

#Only 3 lines are allowed to switch milk and juice
glass3 = glass1
glass1 = glass2
glass2 = glass3

print(glass1 + "  " + glass2)

#User input
name = input("What is your name? : \n")
print("Hello " + " " + name + "!")
print(f"Hello {name}!")

#Band Name
print("#####################################")
print("Welcome to the Band Name Generator")
city = input("What's the name of the city you grew up in? \n")
pet = input("What's your pet's name? \n")

print(f"Your band name could be {city} {pet}")