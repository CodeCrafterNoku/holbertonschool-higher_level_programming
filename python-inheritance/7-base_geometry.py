#!/usr/bin/python3
"""
Module containing BaseGeometry class with area and integer validation
"""


class BaseGeometry:
    """
    BaseGeometry class with area and validation methods
    """

    def area(self):
        """Raises Exception that area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value
        Args:
            name: string name of the value
            value: value to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
