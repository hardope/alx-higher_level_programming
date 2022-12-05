#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    new_list = my_list[:]
    if idx > len(my_list)-1 or idx <= 0:
        return my_list
    else:
        new_list[idx] = element
        return new_list
