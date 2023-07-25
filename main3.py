while True:
    name = input("What is your name? ")
    if name != "":
        break


number = "+254-711-17-44-36"

for digit in number:
    if digit == "-":
        continue
    print(digit, end="")

print("\n")
for age in range(12, 20):
    if age == 18:
        pass
    else:
        print(age)


def hello(name, surname, age):
    print("Hello " + name + " " + surname)
    print("You are " + str(age) + " years old")
    print("Have a nice day!")
hello("Moraa", "Riechi", 24)

def mul(n1, n2):
    result = n1 * n2
    return result
print(mul(89, 10))

#NESTED FUNCTIONS

print(round(abs(float(input("Enter a number: ")))))

#args is a parameter that will pack all arguments
# into a tuple so that a fucntion can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(add(1, 2, 3, 4, 5, 7, 8, 9, 7, 6))

def add1(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 10
    for i in stuff:
        sum = sum + i
    return sum

print(add1(1, 2, 6, 8))