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


















