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
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
