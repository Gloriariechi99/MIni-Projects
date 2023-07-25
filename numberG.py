import random

topRange = input("Type any number: ")

if topRange.isdigit():
    topRange = int(topRange)

    if topRange <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("please type a number next time")
    quit()    

random_number= random.randint(0, topRange)

while True:
    guess = input("make a guess ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please type a number next time")
        continue

    if guess == random_number:
        print("You got it!")
        break

    else:
        print("You got it wrong!")


