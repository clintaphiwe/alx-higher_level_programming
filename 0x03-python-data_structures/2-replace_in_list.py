#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    #Check whether the index(idx) is lesser than 0 and not negative
    if idx < 0:
        return(my_list)
    
    #Check whether index(idx) is greater or equal to the length of the list
    if idx >= len(my_list):
        return(my_list)
    
    #If index is valid, replace the element at that index with the new element
    my_list[idx] = element
    return(my_list)

