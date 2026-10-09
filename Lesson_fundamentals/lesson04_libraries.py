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

