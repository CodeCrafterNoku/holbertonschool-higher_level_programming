#!/usr/bin/python3
"""
Module containing BaseGeometry class with area and integer validation methods
"""


class BaseGeometry:
    """
    BaseGeometry class with area and integer validation methods
    """

    def area(self):
        """Raises an Exception with message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - must be exactly an int (not bool or other numeric type)
        - must be greater than 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
