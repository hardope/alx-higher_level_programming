#!/usr/bin/python3
"""
This program creates a class called MyList that inherits of the class List
"""


class MyList(list):
    """
    This class inherits form the class list an can print it's elements sorted
    """

    def print_sorted(self):
        print(sorted(self))
