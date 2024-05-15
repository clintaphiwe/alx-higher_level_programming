#!/usr/bin/python3
import random

# This line should not change
number = random.randint(-10000, 10000)

def last_digit(num):
    # Take the absolute value of the number to handle negative numbers
    num = abs(num)
    # Get the last digit using the modulus operator
    last_digit = num % 10
    return last_digit

# Get the last digit of the number
last_digit_number = last_digit(number)

# Print the result
if number < 0:
    print("Last digit of", number, "is", -last_digit_number, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", last_digit_number, end=" ")

# Determine if the last digit is greater than 5, equal to 0, or less than 6 and not 0
if last_digit_number > 5:
    print("and is greater than 5")
elif last_digit_number == 0:
    print("and is 0")
elif not (number < 0): 
    print("and is less than 6 and not 0")