#!/usr/bin/python3
"""
A Rectangle Class with the private instance attributes width, height
, public methods and special methods
"""


class Rectangle():
    """
    A Rectangle Class with the private instance attributes width, height,
    public methods and special methods
    """

    def __init__(self, width=0, height=0):
        """
        Constructor of the class Rectangle
          Args:
            - width (default = 0): int
            - heigth (default = 0): int
        """
        self.height = height
        self.width = width

    def area(self):
        """Calculate the area of a Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of a Rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Function to print a Square with #
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        final = [character * self.__width for character in '#' * self.__height]

        return '\n'.join(final)

    def __repr__(self):
        """Returns an “official” string representation of a Rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted"""
        print('Bye rectangle...')

    @property
    def width(self):
        """Getter of the property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Getter of the property value
          Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Getter of the property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Getter of the property value
          Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
