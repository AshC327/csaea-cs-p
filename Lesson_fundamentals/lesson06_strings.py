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

print("\nChallenge 1:")

quote = input("Please input your favorite quote:")

print("Your quote lenth is:", len[quote])
#Accidently deleted challenges trying to make it a comment 

print("\n")
print("Hello", first_name, last_name,"!") #adds a space before the !
print("Hello " + first_name + " " + last_name + "!")
print(f"Hello {first_name} {last_name}!")

print("\nChallenge 3:")

first = input("Please input your first name: ")
last = input("Please input your last name: ")

print(f"Hello {last}, {first}")