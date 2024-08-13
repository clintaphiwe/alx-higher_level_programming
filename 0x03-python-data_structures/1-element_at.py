#!/usr/bin/python3

def element_at(my_list, idx):
    # Check if the index is negative
    if idx < 0:
        return None
    # Check if the index is out of range
    if idx >= len(my_list):
        return None
    # Return the element at the given index
    return my_list[idx]
