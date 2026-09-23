import math

print(7//2,7%2,-7//2)
#3,0,-4 (3,1,-4)

print(int(-5.9), math.floor(-5.9))
#-59,-6 (-5,-6)

print("5"*3,"5"+"5")
#idk (555,55)

print(2**4,math.pow(2,4))
#8,16 (16, 16.0)

print(True+True+True)
#True (3)

print(0.1+0.2==0.3)
#True (False)

print("Zebra" < "apple")
#apple (True) .
  
f = False
t = True
print(not f or t and f)
#False (True)

nums = [34, 52, 3, 64, 32]
print(nums[-len(nums)])
#-5 (34)

for i in range(10,0,-3):
    print(i)
#(10,7,4,1)

x = 5
while x < 10:
    x += 2
    print(x)
#(7,9,11)