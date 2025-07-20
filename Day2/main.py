import pyfiglet

#Python Primitive Data Types

#Integeres
num1 = 9
num2 = 7
result = num1 + num2
print(result)

#Python uses ** to represent exponents
print(num1 ** num2)

#Python supports the order of operations.
print(num1 + 2 * num2)

#Floats
#Pyhton calls any number with a decimal point a **floa**
a = 0.23
b = 4.1
print(a * b)

#Integers and Floats
#When you divide any two numbers, even if they are integers that result in a whole number,
#You will always get a float result.
print(8/2)

#If you mix an **integer** and a float in any other operation, you'll get a float result.
print(4 + 5.1)
print(4.0 * 6 )

#Use underscores when you are writing a long number
decay_time = 45_000_000_000

#BMI Calculator
ascii_banner = pyfiglet.figlet_format(" BMI CALCULATOR ")
print(ascii_banner)

weight = int(input("Enter your weight: \n"))
height = float(input("Enter your height: \n"))

bmi = weight / (height **2)
#print(f"Your bmi is: {round(bmi, 2)}")

if bmi < 18.5:
    print("underweight")
elif bmi <25:
    print("normal weight")
else: print("overweight")