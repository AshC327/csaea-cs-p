import math

#10-------------------------------------------------

groceries = ["milk","eggs", "bread"]

print(groceries)

groceries.insert(0, "apples")
groceries.append("cheese")
groceries.append("rice")

print(groceries)

#3-------------------------------------------------

f = 212
x = f-32
c = x/1.8

print(c)

#4--------------------------------------------------

g = 84

if g >= 90:
    print("A")
elif g >= 80:
    print("B")
elif g >= 70:
    print("C")
elif g >= 60:
    print("D")
else:
    print("F")

#5--------------------------------------------------

p = "csaea2026"
r = "csaea2026"
w = "CSAEA2026"

if r == p:
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
tips = print("tip =")
print(tip)
total = tip+bill
print("total =")
print(total)

#8----------------------------------------------------
first = "Ada"
last = "Lovelace"
school = "CSAEA"

print(f"Hello, my name is {first} {last} from {school}")

#6-------------------------------------------------------

plate = 2242
if plate%2==0:
    print("park on east side")
else:
    print("park on west side")

#9------------------------------------------------------------

cart = [12, 5, 30, 8]
print(f"list:{cart}")
print(f" Items = {(len(cart))}")