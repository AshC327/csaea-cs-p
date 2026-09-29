import math

#10-------------------------------------------------

groceries = ["milk","eggs", "bread"]

print(groceries)

groceries.insert(0, "apples")
groceries.append("cheese")
groceries.append("rice")

print(groceries)

#3-------------------------------------------------

fahrenheit = 212
math = fahrenheit-32
celsius = math/1.8

print(celsius)

#4--------------------------------------------------

grade = 84

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

#5--------------------------------------------------

password = "csaea2026"
right = "csaea2026"
wrong = "CSAEA2026"

if right == password:
    print("Access Granted")
else:
    print("Access Denied")

#20----------------------------------------------------

speedlimit = 55
speed = 71

if speed > speedlimit:
    print("Fine: $100")
else:
    print("Speed limit: okay")

#7----------------------------------------------------

hieght = True
age = True
withparent = True


if hieght and age and withparent:
    print("You may ride")
else:
    print("You may not ride")

#1----------------------------------------------------
bill = 50
tip = 0.2*bill
print(f"Tips = {tip}")
total = tip+bill
print(f"total = {total}")

#8----------------------------------------------------
first = "Ada"
last = "Lovelace"
school = "CSAEA"

print(f"Hello, my name is {first} {last} from {school}")

#6-------------------------------------------------------

plate = 4827
if plate%2==0:
    print("park on east side")
else:
    print("park on west side")

#9------------------------------------------------------------
import math 

cart = [12, 5, 30, 8]
print(f"list:{cart}")
print(f" Items = {(len(cart))}")
result = sum(cart)
print(f"Total: ${result}")

#2------------------------------------------------------------
import math 

students = 23
slices_per_student = 2
slices_per_pizza = 8

problem1 = slices_per_pizza/slices_per_student
problem2 = students/problem1
answer = (math.ceil(problem2))
print(f"{answer} pizzas are needed")

#11------------------------------------------------------------

start = 10

for z in range(10, 1, -1):
    print(z)
print("Liftoff!")

#12------------------------------------------------------------

number = 7
multiply = 1


for x in range(1,11):
    sum = number*multiply
    print(f"{number} x {multiply} = {sum}")
    multiply += 1

#13------------------------------------------------------------

savings = 0
weekly_deposit = 15
goal = 100
week = 1

print(f"Weeks: {week}")
print(f"Saved: ${savings}" + "\n")

while savings < goal:
    week += 1
    savings += weekly_deposit
    print(f"Weeks: {week}")
    print(f"Saved: ${savings}" + "\n")

#14---------------------------------------------------
#DIDN'T UNDERSTAND THIS ONE

#???????????????
#???????????????
#???????????????

#15---------------------------------------------------

#uses elements that i dont understand from 14

#?????????????????????????????????

#16---------------------------------------------------

import math

area = 49

total = math.sqrt(49)
print(f"{total} feet for one side.")

#17---------------------------------------------------

minutes_parked = 60
block_length = 15
cost_per_block = 1

problem1 = minutes_parked/block_length
problem2 = problem1*cost_per_block
print(f"You owe ${problem2}")

