import time 
import random

player_name = input("Enter your name please: ")
time.sleep(1)
print(f"Well, then hello {player_name}")

time.sleep(2)
color = input("Lets go to know you, favorite color? ")
time.sleep(1)
if color == "White":
    print("That's mine too!")
elif color == "white":
    print("That's mine too!")
else:
    print(f"Eh, {color} is okay. I personally like white")

time.sleep(1)

print("Well then, lets get started!")

guess = input("Heads or tails? ")

choice = guess

coin = random.choice(1,2)

if guess == "Heads":
    guess = 1
elif guess == "heads":
    guess = 1
else: 
    guess = 2

time.sleep(1)
print("I'm flipping a coin")

time.sleep(1.5)

print(coin)
if coin == guess:
    print(f"You were right! it was {choice}")
else:
    print(f"Well. It wasn't {choice}")