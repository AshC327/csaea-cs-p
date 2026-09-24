import math

#make a list starting with apples, and includes cheese and rice

groceries = ["milk","eggs", "bread"]

print(groceries)

groceries.insert(0, "apples")
groceries.append("cheese")
groceries.append("rice")

print(groceries)

#-------------------------------------------------

f = 212
x = f-32
c = x/1.8

print(c)

#--------------------------------------------------

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

#--------------------------------------------------

p = "csaea2026"
r = "csaea2026"
w = "CSAEA2026"

if r == p:
    print("Access Granted")
else:
    print("Access Denied")

#----------------------------------------------------
