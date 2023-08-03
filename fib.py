import fibo

fibo.fib(1000)
fibo.__name__
fibo.fib2(100)

fib = fibo.fib
fib(500)

import random

for i in range(8):
    print(random.randint(10, 20))


members = ['Jonn', 'Allan', 'Smith', 'Mary', 'Judith', 'Tabitha']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
    

dice = Dice()
print(dice.roll())


from pathlib import Path


path = Path()
for file in path.glob('*'):
    print(file)


