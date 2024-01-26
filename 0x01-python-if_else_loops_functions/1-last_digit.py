#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = 0
if number / 10 == 0:
    l_digit = number
elif number / 100 == 0:
    l_digit = number % 10
elif number / 1000 == 0:
    l_digit = number % 100
    l_digit = l_digit % 10
else:
    l_digit = number % 1000
    l_digit = l_digit % 100
    l_digit = l_digit % 10
if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is zero")
else:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
