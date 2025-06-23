#!/usr/bin/python3
"""Defines a Square class with private size attribute"""


class Square:
    """Class that defines a square with private instance attribute size"""
    
    def __init__(self, size):
        """Initializes the square with a given size
        
        Args:
            size: size of the square
        """
        self.__size = size
