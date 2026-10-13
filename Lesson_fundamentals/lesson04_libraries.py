#MATH

import math

math.ceil(6.7)   #round up, 7
math.floor(6.7)  #round down, 6
math.sqrt(9)     #square root, 3
math.pow(2,4)    #___ to the power of ____, 16
math.pi          #3.141592653589793, stops there

#CHALLENGE 1 

print("\nChallenge 1:")

diameter = 14
radius = diameter/2
circle_area = math.pi*math.pow(radius,2)
print(circle_area)
print(math.ceil(circle_area))
print("\n")

#PYTHON RANDOM LIBRARY

#Python's library is a pseudorandom number generator

seed = 9

num1 = seed/1.2345

num2 = num1+seed

num3 = num2*num1

print("Challenge 2:")
print(math.ceil(num3))
print("\n")

#BONUS CHALLENGE make a random number generator for 1 - 10
print("Bonus Challenge:")
seed = 327
step1 = seed*7
step2 = step1/12
step3 = step2 % 10
print(math.ceil(step3))
print("\n")



#RANDOM
print("Import Random:")


import random

random_integer = random.randint(1,100)
print(random_integer)

random_float = random.random()
print(random_float)

my_list = ["taco", "burrito", "enchilada", "quesadilla"]
random_selection = random.choice(my_list)
print(random_selection)

random.shuffle(my_list)
print(my_list)

print("\n")

print("Challenge 3:")
#Simulate rolling a six sided dice

die_roll = random.randint(1,6)
print(f"You rolled a: {die_roll}")


print("\nChallenge 4:")

num = random.randint(1,75)
calc1 = math.sqrt(num)
calc2 = math.ceil(calc1)
print(f"Unrounded square root: {calc1}\nRounded square root: {calc2}")

print("\nChallenge 5:")

base = random.randint(1,6)
exponent = random.randint(1,6)
equation = base**exponent
result = int(equation)
print(f"Result: {result}")

#MESSING ARROUND

magic8_ball = random.randint(1,5)

if magic8_ball == 1:
    print("Yes")
elif magic8_ball == 2:
    print("No")
elif magic8_ball == 3:
    print("Maybe")
elif magic8_ball == 4:
    print("Ask Again Later")
else:
    print("I do not know")

import time

time.sleep(1) #delays one second