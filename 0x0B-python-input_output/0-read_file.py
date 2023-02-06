#!/usr/bin/python3
"""
This program reads files
"""


def read_file(filename=""):
    """
    This function read a file and print it's content
    """

    with open(filename, encoding="utf-8") as _file:
        print(_file.read(), end="")
