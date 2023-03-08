#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    remainde = number % -10
else:
    remainde = number % 10
if remainde == 0:
    print(f'Last digit of {number} is {remainde} and is 0')
elif remainde < 6 and remainde != 0:
    print(f'Last digit of {number} is {remainde} and is less than 6 and not 0')
elif remainde > 5:
    print(f'Last digit of {number} is {remainde} and is greater than 5')
