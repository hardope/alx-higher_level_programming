#!/usr/bin/python3
"""
This program use the inherit for create a new Rectangle
"""


prevRectangle = __import__('8-rectangle').Rectangle


class Rectangle(prevRectangle):
    """
    Class Rectangle based in BaseGeometry and other rectangle
    """

    def __init__(self, width, height):
        """Constructor of new Retangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """This method return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This method return the representation of the Rectangle"""
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
