class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

point = Point(10, 20)
print(point.x)

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.y)
# point1.draw()

# point2 = Point()
# point2.x = 987
# print(point2.x)

class Person:
    def __init__(self, name) -> None:
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


gloria = Person("Gloria Moraa")
print(gloria.name)
gloria.talk()


class Persons:
    def __init__(par1, name, age, prof):
        par1.name = name
        par1.age = age
        par1.prof = prof

    
    def __str__(par1) -> str:
        return f"{par1.name}({par1.age})"
    
    def func1(par1):
        print("Hello my name is " + par1.name + ", I'm " + str(par1.age) + " years old")


p1 = Persons("Gloria Riechi", 24, "Software engineer")
p1.age = 23
print(p1.prof)
del p1.prof
p1.func1()

#inheritance

class Mammal:
    def walk(self):
        print("Has four limbs")


class Cat(Mammal):
    pass


class Dog(Mammal):
    def bark(self):
        print("Barks")


cat1 = Cat()
cat1.walk()

dog1 = Dog()
dog1.bark()
dog1.walk()