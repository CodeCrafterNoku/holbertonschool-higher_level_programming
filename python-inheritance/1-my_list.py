#!/usr/bin/python3
"""
Module containing MyList class that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list with additional print_sorted method
    """

    def print_sorted(self):
        """Prints and returns the list in sorted ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
