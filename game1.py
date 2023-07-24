print("Welcome to my computer quiz!")


playing = input("do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()
print("Okay! let the game start :)")

score = 0

answer = input("What does CPU stnd for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")


answer = input("What PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")