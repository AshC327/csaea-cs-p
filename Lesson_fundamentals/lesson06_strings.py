greeting = "Hiiii"
first_name = "Ashlyn"

print(f"\n{greeting} {first_name}")

#strings have indexes
# 0 1 2 3 4
# H E L L 0

#spaces are also indexes
# 012
# h i 

word = "HELL0"
second_letter = word[1]

print(f"\n{second_letter}")

something = "supercalifragilisticexpialidocious"
print("\nFirst letter is:", something[0])

print("The last letter is:", something[-1])

print("Range of letters (non-inclusive):", something[5:9])

print("First five letters:", something[0:5])
#or
print("First five letters (2):", something[:5])

print("Everything after the first five letters:", something[5:])
print("Last seven letters:", something[-7:])

print("Every other character:", something[::2]) #nothing between the colon is a hidden 0 (zero)

print("String in reverse:", something[::-1])

last_name = "Cooper"

length = len(last_name) #includes spaces

print(f"Length of string, {last_name}, is {length}")

# print("\nChallenge 1:")

# quote1 = input("Please input your favorite quote:")

# print("Your quote lenth is:", len[quote1])
#Accidently deleted challenges trying to make it a comment 

print("\n")
print("Hello", first_name, last_name,"!") #adds a space before the !
print("Hello " + first_name + " " + last_name + "!")
print(f"Hello {first_name} {last_name}!")

# print("\nChallenge 3:")

# first = input("Please input your first name: ")
# last = input("Please input your last name: ")

# print(f"Hello {last}, {first}")

print("\n")

character = "spOngBoB SQauRepAntS"
lower = character.lower()
upper = character.upper()
title = character.title()
print(f"Lowercase: {lower}")
print(f"Uppercase: {upper}")
print(f"Title: {title}")

print("\n")

sentence = "This is a sentence"
new_sentence = sentence.replace("a","a longer")
print(sentence)
print(new_sentence)

groceries = "milk,bread,chese,butter"
print("Original string:", {groceries})

#split the string into a python list, based on a 'delimiter'

items = groceries.split(",")

print("Split string:", items)

#join the list together into a string

joined = " and ".join(items)
print("Joined together:", joined)
print("\n")
print(type(groceries))
print(type(items))
print(type(joined))

print("\nChallenge ?:")
word = input("Please type in a word: ")
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())
print("In reverse:", word[::-1])