#math operators; +, -, *, /, %, **, //, 

add = 27+300
print("add: \t\t", add)

subtract = 6-7
print("subtract: \t", subtract)

multiply = 7*2
print("multiply: \t", multiply)

float_divide = 10/3
print("float divide: \t", float_divide)

integer_divide = 7//2
print("integer divide: ", integer_divide)

mod = 7%2
print("modulus: \t", mod)

exponent = 7 ** 2
print("exponent: \t", exponent)

#PEMDAS (its pemdas)

result1 = 2+3*4
print("result1: \t", result1)

result2 = (2+3)*4
print("result2: \t", result2)

result3 = 2**3*4
print("result3: \t", result3)

result4 = 5+2**3*(4-1)
print("result3: \t", result4)
print("\nCHALLENGES :3\n")

#CHALLENGE 1

height = 5
width = 8
rectangle_area = height*width

print("Challenge 1 \t", rectangle_area)
print("\n")
#CHALLENGE 2

radius = 7
circle_area=3.14*7**2
print("Challenge 2 \t", circle_area)
print("\n")
#CHALLENGE 3
print("Challenge 3:")
book = 12.99
notebook = 3.5
total_cost = 3*book+4*notebook

print(f"Book:  \t\t ${book}\nNotebook:  \t ${notebook}\nTotal cost:  \t ${total_cost}\n")

#CHALLENGE 4

number = 57
problem = number%2
print("Challenge 4:")
if problem == True:
    print(f"{number} is Odd")
else:
    print(f"{number} is Even")

#Other of 4

print("\nChallenge 4 Test:")
if problem == 1:
    print("Odd")
else:
    print("Even")