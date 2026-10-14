#USER INPUT

#like a print statement

#any input is taken in as a string

# name = input("Input you name: ")
# print(f"Well then hello {name}\n")

# age = input("Enter your age please: ")
# print(f"Good to know your {age}\n")

# age_convert = int(age)

# print(type(age_convert))

# height = float(input("Enter your height: "))
# print (height,"\n")

print("Challenge 1:")

color = input("So, I want to get to know you better. Favorite Color: ")
print(f"I see, {color} is a good choice")

print("\nChallenge 2:")

num1 = int(input("Hey, can I get a number: "))
num2 = int(input("How about one more: "))
result = num1 + num2
print(result)

print("\nChallenge 3:")

diameter = int(input("Can you give a number, for an equation: "))
radius = diameter/2
equation = (radius**2)*3.14

print(f"Heres the area of a circle with your number: {equation}")

print("\nChallenge 4:")

#ask he user for a number
#custom sided dice

dice = (f"Give me a number for a sided die: ")


import random

roll = random.choice(1,dice)
print(roll)