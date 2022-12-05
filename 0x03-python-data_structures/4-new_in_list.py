#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    new_list = my_list[:]
    if len(my_list) > idx >= 0:
        new_list[idx] = element
        return new_list
