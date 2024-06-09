#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    last_digit = number % 10
    print("The last digit of {} is {}.".format(number, last_digit))
    return last_digit

# Example usage:
number = -1204
print_last_digit(number)