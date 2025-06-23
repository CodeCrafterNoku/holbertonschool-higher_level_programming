#!/usr/bin/python3
"""Function that adds two integers"""

def add_integer(a, b=98):
    """Adds two integers
    
    Args:
        a: first number (must be int or float)
        b: second number (must be int or float, defaults to 98)
    
    Returns:
        Sum of a and b as integer
        
    Raises:
        TypeError: If a or b are not integers/floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
