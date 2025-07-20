import pyfiglet

ascii_banner = pyfiglet.figlet_format("Welcome to the tip calculator")
print(ascii_banner)

bill = float(input("What was the total bill? "))
tip = int(input("how much tip would you like to give? 10, 12, or 15 "))
people = int(input("How many persons to split the bill? "))

tip_amount = (tip /100) * bill
payment_per_person = (tip_amount + bill) / people

print(f"Each person should pay {payment_per_person}")