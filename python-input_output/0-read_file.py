#!/usr/bin/python3
"""
Module containing function to read and print file contents
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout
    
    Args:
        filename: name of the file to read
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
