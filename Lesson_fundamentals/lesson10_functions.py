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

print("Chalenge 1\n")

list = []


def doubler(number, times):
    for i in range(times):
        list.append(number)
        number = number * 2

one = 2
two = 5
test = doubler(one,two)
print(list)