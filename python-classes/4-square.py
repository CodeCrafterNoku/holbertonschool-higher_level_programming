#!/usr/bin/python3
"""Defines a Square class with size property and area calculation"""


class Square:
    """Class that defines a square with size validation and area calculation"""
    
    def __init__(self, size=0):
        """Initialize the square with size
        
        Args:
            size: size of the square (default 0)
        """
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        """Getter for size property
        
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size property with validation
        
        Args:
            value: new size value
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area
        
        Returns:
            The area of the square (size squared)
        """
        return self.__size ** 2
