#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

numb_in_str = repr(number)
last_digit_str = numb_in_str[-1]
last_digit = int(last_digit_str)

if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater 5")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
elif last_digit < 6 and last_digit != 0:
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
