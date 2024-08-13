#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    #Checks whether idx(index) is lesser than 0 or idx(index) is equal or greater 
    # than the list and prints the list 
    if idx < 0 or idx >= len(my_list):
        print("{}".format(my_list))

        print("{}".format(my_list[:]))
    #Assigns my_list to new_list and then assigns idx(index) the new element                
    new_list = my_list[:]
    new_list[idx] = element
    print("{}".format(new_list))
