#!/usr/bin/python3
"""
This program improves a previous Square
"""


PrevSquare = __import__('10-square').Square


class Square(PrevSquare):
    """
    Improved Class Square
    """

    def __init__(self, size):
        """Constructor of the improved Square"""
        super().__init__(size)

    def __str__(self):
        """String representation of Square"""
        return '[Square] {0:d}/{0:d}'.format(self.__size)
