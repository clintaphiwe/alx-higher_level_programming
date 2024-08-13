#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Create a formatted string for each row
            row_str = ' '.join('{:d}'.format(num) for num in row)
            print(row_str)
