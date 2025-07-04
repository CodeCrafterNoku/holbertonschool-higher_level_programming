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
        - must be an integer
        - must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
