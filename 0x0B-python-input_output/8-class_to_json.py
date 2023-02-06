#!/usr/bin/python3
"""
This program return the dict representation of a instance of Class.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    Args:
      - obj: instance of class
    """

    return (obj.__dict__)
