#CONDITIONALS
#key things: ==, !=, <, >, <=, >=
#equal too, not equal, less than, greater than, less than or equal to, greater than or equal to

print(3==2) #False
print(7!=4) #True
print("hello" == "hell0") #false
print(4<5) #True

print("")

#if

num = 12

if num == 10:
    print("Your num is = 10")

#if else

num = 12

if num <= 12:
    print("Your num is <= 12")
else:
    print("Your num is > 12")

#if elif else

temp = 32

if temp >= 90:
    print("Hot!")
elif temp >= 70:
    print("Nice")
else:
    print("Cold!")

print("")

x = 20.000000000000001
y = 20

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
else:
    print("x is less than y")

age = 16
has_permission = True

if age >= 16 and has_permission:
    print("You can drive")
else:
    print("You can't drive")

#logical operators: 'or' and 'not'

day = "sunnday"
day = day.lower()

if day == "saturday" or day == "sunday":
    print("It's a weekend!")
else:
    print("It's a weekday :(")

print("\n--- Using 'is' and 'not' ---\n")

if day is not "monday":
    print("Thankfully it's not Monday")
else:
    print("Sigh, It's a Monday")

print("\n\nChallenge 1\n")

#age = input("Please input your age: ")
age = int(age)

if age >= 18:
    print("You can watch any rated movie")
elif age >= 13:
    print("You can watch PG and PG movies")
else:
    print("You can only watch PG movies")

print("\nChallenge 2\n")

year = 1900

print(year/100)


if year%400 == 0 :
    print(f"{year} is a leap year.")
elif year%4 == 0:
    if year%100 == 0:
        print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
