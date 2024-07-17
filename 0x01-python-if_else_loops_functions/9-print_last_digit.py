#!/usr/bin/python3
def print_last_digit(number):
    l_digit = 10
    if number < 0:
        number = -number
    while l_digit > 9:
        l_digit = number % 10
        number = number / 10
    print(l_digit, end='')
    return (l_digit)
