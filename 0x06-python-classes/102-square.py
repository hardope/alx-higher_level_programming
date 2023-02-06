#!/usr/bin/python3
"""Create a Class Square with size, method of area and getters & setters"""


class Square:
    """Class - Square"""

    def __init__(self, size=0):
        """Constructor of a Square with the size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def __lt__(self, other):
        """Compare operator <"""
        return (self.area() < other.area())

    def __le__(self, other):
        """Compare operator <="""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """Compare operator >"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Compare operator >="""
        return (self.area() >= other.area())

    def __eq__(self, other):
        """Compare operator =="""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Compare operator !="""
        return (self.area() != other.area())

    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
        if ((type(value) is int) or (type(value) is float)):
            if (value < 0):
                raise (ValueError("size must be >= 0"))
            else:
                self.__size = value
        else:
            raise (TypeError("size must be a number"))
