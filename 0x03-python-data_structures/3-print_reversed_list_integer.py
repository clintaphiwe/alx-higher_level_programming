#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    #Iterate over the list in reverse order
    for i in range(len(my_list) - 1, -1, -1):
        #Print each integer in the list, one per line
        print("{}".format(my_list[i]))
