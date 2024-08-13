#!/usr/bin/python3

def element_at(my_list,idx):
    # Check whether the index(idx) is lesser than 0 or not negative
    if idx < 0:
        return None
    # Check whether index(idx) is greater or equal to the length of the list
    elif idx >= len(my_list):
        return None
    # If index is valid, return the element at that index
    return "Element at index {} is {}".format(idx ,my_list[idx])
