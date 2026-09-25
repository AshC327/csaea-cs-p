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

sl = 55
s = 71

if s > sl:
    print("Fine: $100")
else:
    print("Speed limit: okay")

#7----------------------------------------------------

h = 50
a = 8
ha = True

hh = h>=48
aa = a<10

if hh is True:
    hh = True
else:
    hh = False

if aa is True:
    aa = True
else:
    aa = False

if ha is aa:
    z = True
else:
    z = False

if hh == aa == z:
    print("You may ride")
else:
    print("You may not ride")

#----------------------------------------------------