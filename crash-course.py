import math

# comment
print ("word")

# Variable declarations and data types

a = 4 #interger
b = 5.5 #float
c = "CSAEA" #sting
d = False #boolean

print (c, a, b, d)

#operators
# + - / *   % ** //

# += -= /=

e = 8 // 8

#f-string

print (f"e is equal to {e}")

e -= 7
e += 12

print (f"e is now equal to {e}")

# comparisons (booleans, which always return True or False)

#< > <= >= !=

print(4<5)

print(1!=5)

isequal = 5==6

print(isequal)

i = "Yes" == "YES"

print (i)

# logical operators

f = False
t = True

print(not f) #true
print(f and t) #false
print(f or t) #true
print(f or t and not f) #true

#CASTING

g = 5.5
print(g)
g = int(5.5)
print(g)

s1 = "Goodnight" 
s2 = " and "
s3 = "Goodbye" 
end = s1 + s2 + s3
print(end)

end += ". :)"
print (end + "\n" + "\n")

#Math Library

print (math.sqrt(14))
print(math.ceil(3.14))
print(math.floor(5.87))
