#**kwargs parameter tha packs all arguments into a dictionary
#so that a fucntion can accepsta varying amount of keyword arguments

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title = "Miss.", first="Gloria", middle="Moraa", last="Riechi")
print("\n")

price = 1000000

goodCredit = False

if goodCredit:
    down_payment = int(0.1 * price)
else:
    down_payment = int(0.2 * price)

print("The down payment for this buyer is", str(down_payment) + " dollars")

highIncome = True
good_credit = False

if good_credit and not highIncome:
    print("Customer is eligible for a loan")
else:
    print("Customer is not eligible for a loan")

name1 = input("Please enter your name ")

if len(name1) < 3:
    print("Name must be more than three characters")
elif len(name1) > 50:
    print("Name must be less than fifty characters")
else:
    print("Name looks good!")

weight = input("Please enter your weight ")
unit = input("Lbs or kgs ")
 
if unit.lower() == "kgs":
    weight_lbs = float(weight) * 2.20462262185
    print("You weigh", str(weight_lbs) + " pounds")
else:
    weight_kgs = float(weight) / 2.20462262185
    print("You weigh", str(weight_kgs) + " kilograms")

#handling errors
try:
    age  = int(input("Age: "))
    print(age)
    income = int(input("Income: "))
    risk = income / age
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid value")

















