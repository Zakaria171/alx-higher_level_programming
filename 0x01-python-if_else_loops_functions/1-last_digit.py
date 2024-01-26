#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0
if number / 10 == 0:
    last_digit = number
elif number / 100 == 0:
    last_digit = number % 10
elif number / 1000 == 0:
    last_digit = number % 100
    last_digit = last_digit % 10
else:
    last_digit = number % 1000
    last_digit = last_digit % 100
    last_digit = last_digit % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
