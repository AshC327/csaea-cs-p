#Python: Functions
#Suedocode: Procedures

#Function: blocks of code that you can use again and again and again

def new_line():
    print()

def say_hi():
    print("hi")


def say_bye():
    print("bai")

say_hi()
say_bye()
say_hi()
say_bye()

new_line()

# Functions more commonly RETURN data

def express_this(e): #in parenthesis is called a parameter
    return(e)

expression = express_this(3+27) #in parenthesis is an argument

print(expression)

new_line()

def greeter(name):
    return f"Hi {name}"

first = greeter("Ash")
second = greeter("Syd")
third = greeter("Raaga")

print(f"{first}\n{second}\n{third}")

new_line()

def remainder(a,b):
    return a%b

result = remainder(27,3)
print(result)

new_line()

def is_far(distance):
    if distance >= 100:
        return "That's far!"
    if distance < 100 and distance > 20:
        return "That's not too far"
    else:
        return "That's pretty close!"

one = is_far(327)
two = is_far(50)
three = is_far(5)

print(f"{one}\n{two}\n{three}")

new_line()

print("Chalenge 1:")

list = []


def doubler(number, times):
    num = number
    for i in range(times):
        number = number * 2
        list.append(number)
    return list

one = 1
two = 5
test = doubler(one,two)
print(test)

print("\nChallenge 2:")

def addition(a,b):
    print(a+b)
    return a+b

def subtraction(c,d):
    print(c-d)
    return(c-d)

def multiplication(e,f):
    print(e*f)
    return e*f

def division(g,h):
    print(g/h)
    return(g/h)

addition(3,27)
subtraction(9,1)
multiplication(7,7)
division(6,3)

print("\nChallenge 3:")

def average(a,b,c,d,e):
    temp = a+b+c+d+e
    print(temp/5)
    return(temp/5)

average(90,80,95,67,100)

print("\nChallenge 4:")

def even_odd(a):
    if a%2 == 0:
        print("Even")
        return "Even"
    else:
        print("Odd")
        return "Odd"

even_odd(327)
    
print("\nChallenge 5:")

def anaylize_word(word):
    vowels = 0
    consonants = 0
    for letter in word:
        if letter in "aeiou" or letter in "AEIOU":
            vowels += 1
        else:
            consonants += 1
    print(f"{word} has {vowels} vowels and has {consonants} consonants")
    return f"{word} has {vowels} vowels and {word} has {consonants} consonants"

anaylize_word("kipsulheris")