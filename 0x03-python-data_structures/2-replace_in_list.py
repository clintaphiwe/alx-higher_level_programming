#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    #Check whether the index(idx) is lesser than 0 and not negative
    if idx < 0:
        print("{}".format(my_list))
    #Check whether index(idx) is greater or equal to the length of the list
    elif idx >= len(my_list):
        print("{}".format(my_list))
    #If index is valid, replace the element at that index with the new element
    else:
        print("{}".format(my_list))
        my_list[idx] = element
        print("{}".format(my_list))
