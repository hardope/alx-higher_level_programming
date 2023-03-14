#!/usr/bin/python3
"""String manipulations"""


def say_my_name(first_name, last_name=""):
    """Prints a string.
    Validates string inputs, the display
    the full name
    """
    if type(first_name) != str:
        raise TypeError("first name must be a string")
    if type(last_name) != str:
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
