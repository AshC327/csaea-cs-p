import time

#LOOPS a.k.k (ITERATION/to iterate)
#Types: for-loops, while-loops

#for-loop

animals = ["cat", "dog", "deer", "fox"]

print(f"\n{animals}")

for a in animals:
    print("Now I'm petting a", a)
    #time.sleep(1)

#looping x amount of times
print("")

for x in range(5):
    print(f"Loop number {x}")

#range(start, stop, step)
print("")

for num in range(3,27,5):
    print(f"Printing number: {num}")

#string iteration
print()

word = "supercalifragilisticexpialidocious"
print(word)

letter_list = []

for letter in word:
    letter_list.append(letter)

print(letter_list)

print("\nChallenge 1\n")

total = 0
for i in range(1, 11):
    total = total + i
    print(f"Loop {i}: {total}")

print("\n")

#while-loop

count = 0

while count < 5:
    print(f"Loopin: -- we are on loop index #{count}")
    count += 1
    time.sleep(.25)

print()

user_input = ""
while user_input != "exit":
    user_input = input("Type exit to escape: ")

# LOOP CONTROLS

for i in range(1,11):
    if i == 3:
        print("Skipping 3")
        continue #skips this iteration
    if i == 6:
        print("Take a break your at 6 ")
        break #stops loop
    if i == 9:
        pass #place holder
    print("Number:", i)

print("\nChallenge 2\n")

user_guess = input("Please input a number as your guess: ")

num = "7"
while user_guess != num:
    user_guess = input("Nope wrong :) try again: ")

print(f"Your right, it was {num}!")