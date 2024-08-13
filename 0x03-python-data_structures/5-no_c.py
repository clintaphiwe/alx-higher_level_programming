#!/usr/bin/python3

def no_c(my_string):
    # Initialize an empty list to collect characters that are not 'c' or 'C'
    result = []
    
    # Iterate over each character in the input string
    for char in my_string:
        # If the character is not 'c' or 'C', add it to the result list
        if char != 'c' and char != 'C':
            result.append(char)
    
    # Join the list of characters into a single string and return it
    return ''.join(result)
