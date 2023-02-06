#!/usr/bin/python3
"""
This program have a class with a validator and an error
"""


class BaseGeometry():
    """
    This class contain a method not implemented and a validator
    """

    def area(self):
        """
        This function raise an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate if value is a integer.
        Args:
          - name: str
          - value: int
        """
        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
