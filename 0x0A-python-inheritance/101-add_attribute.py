#!/usr/bin/python3
"""
This program will try to add attributes to classes if it possible
"""


def add_attribute(obj, key, value):
    """
    This function will try to add a new attribute
    to a class if it possible, throws an Exception if can't
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
