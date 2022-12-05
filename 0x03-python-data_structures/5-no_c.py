#!/usr/bin/python

def no_c(my_string):
    new_string = ""

    for i in my_string:
        if i == 'c':
            pass
        else:
            new_string+=i
    return new_string
