#!/usr/bin/bash

def print_reversed_list_integer(my_list=[]):
    for i in my_list.reverse():
        print("{:d}".format(i))
