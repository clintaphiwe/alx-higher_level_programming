#!/usr/bin/python3
def to_uppercase(input_string):
    output_string = ""
    for char in input_string:
        if char.islower():
            output_string += chr(ord(char) - 32)
        else:
            output_string += char
    return output_string
