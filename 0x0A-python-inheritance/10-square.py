#!/usr/bin/python3
"""
This program create a Square from a Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Squared based from Rectangle"""
    def __init__(self, size):
        """Constructor of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of a Square"""
        return self.__size ** 2
