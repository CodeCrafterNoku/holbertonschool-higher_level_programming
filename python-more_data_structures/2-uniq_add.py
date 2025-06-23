#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_integers = set(my_list)
    # Return the sum of unique integers
    return sum(unique_integers)
