#MATH FUNCTIONS
import math

pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(625))
list1 = [4, 7, 89, 98, 456]
print(max(list1))

temp = int(input("What is the temperature today in degrees celcius? "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("you can go for a walk")
elif temp < 0 or temp > 30:
    print("the temperature is not conducive today!")
    print("You cannot go outside")


name = ""

while len(name) == 0:
    name = input("Please enter your name: ")

print("Hello " + name)

for i in range(50, 100, 2):
    print(i)

import time

for sec in range(10, 0, -1):
    print(sec)
    time.sleep(1)
print("Happy New Year:)")