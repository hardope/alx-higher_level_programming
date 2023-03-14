#!/usr/bin/python3
"""Printing square"""


def print_square(size):
    """Prints a square with the character '#'"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
