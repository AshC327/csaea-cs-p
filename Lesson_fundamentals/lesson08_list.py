#LISTS




empty_list = []

#create lsits

animals = ["cat", "dog", "cow", "bird"]
numbers = [2, 4, 6, 8, 10]
mixed = ["word", 42, True, 3.27]

print(animals)
print(numbers)
print(mixed)

print()

#print the third one
print(animals[2])
#print the last number
print(numbers[-1])
#print the first
print(mixed[0])

print()

#swap something for someting else
print(animals)
animals[-1] = "deer"
print(animals)

print()

#add elements
print(animals)
animals.append("ferret")
print(animals)

print()

#inserting
print(animals)
animals.insert(2,"bunny") #becomes index 2 and not after index 2
print(animals)

print()

#remove
print(animals)
animals.remove("cow")
print(animals)

print()

#cut (pop) off the last element of the list and storing it
print(animals)
last_animals = animals.pop()
print(animals)
print(last_animals)

print()

print("Challenge 1\n")

nums = [1, 2, 3, 4, 5, 6]

print(nums)
#new_num = input("Please input a number: ")
#new_num = int(new_num)

#nums[2] = new_num

#print(nums)

print("\nChallenge 2\n")

shopping = []
print(shopping)
shopping.append("cheese")
print(shopping)
shopping.append("chocolate")
print(shopping)
shopping.append("pretzels")
print(shopping)
shopping.insert(1, "bread")
print(shopping)
shopping.remove("chocolate")
print(shopping)

print()

number = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Length of list:", len(number))
print("Min:", min(number))
print("Max:", max(number))
print("Sum:", sum(number))

print()

number.sort()
print(number)
print()
animals.sort()
print(animals)

number.reverse()
print(number)

word = "cat"

if word in animals:
    print(f"I FOUND {word}")
else:
    print(f"i didn't find {word}")

print("\nChallenge 3\n")

something = [3.27, 3.10, 6.03, 9.03, 7.07]
print("Length", len(something))
print("Minimum", min(something))
print("Maximum", max(something))
print("Sum", sum(something))
something.sort()
print("Sort", something)