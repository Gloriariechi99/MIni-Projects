import math
import random
import sys
import re
import os

def check_number(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 5:
            print("Weird")
        else:
            print("Not Weird")

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    check_number(num)

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
ad = a + b
print("The sum of ", str(a) + " and ", str(b)  + " is ", str(ad))
sub = a - b
print("The difference of ", str(a) + " and ", str(b) + " is ", str(sub))
mul = a * b
print("The product of ", str(a) + " and ", str(b) + " is ", str(mul))
int_div = a // b
print("The integer division of ", str(a) + " and ", str(b) + " is ", str(int_div))
float_div = a / b
print("The float division of ", str(a) + " and ", str(b) + " is ", str(float_div))
