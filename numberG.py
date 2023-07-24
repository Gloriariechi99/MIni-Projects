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
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
else:
    print("please type a number next time")
    continue


