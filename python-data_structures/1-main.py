#!/usr/bin/python3
element_at = __import__("1-element_at").element_at

my_list = [1, 2, 3, 4, 5]
print("Element at index 3 is {}".format(element_at(my_list, 3)))  # Valid
print("Element at index -1 is {}".format(element_at(my_list, -1)))  # Negative
print("Element at index 5 is {}".format(element_at(my_list, 5)))  # Out of range
