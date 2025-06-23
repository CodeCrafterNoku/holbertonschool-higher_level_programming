#!/usr/bin/python3
"""
add_integer - Adds two integers or floats and returns the result as an integer.
"""

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
