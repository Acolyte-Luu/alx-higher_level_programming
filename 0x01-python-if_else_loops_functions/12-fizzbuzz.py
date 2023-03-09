#!/usr/bin/python3
def fizzbuzz():
    fizz = "Fizz"
    buzz = "Buzz"
    fizzbuzz = "FizzBuzz"
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            number = fizzbuzz
        elif number % 5 == 0:
            number = buzz
        elif number % 3 == 0:
            number = fizz
        print(number, end=' ')
