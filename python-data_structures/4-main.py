#!/usr/bin/python3
new_in_list = __import__("4-new_in_list").new_in_list

my_list = [1, 2, 3, 4, 5]
print(new_in_list(my_list, 3, 9))  # Valid
print(new_in_list(my_list, -1, 9))  # Negative
print(new_in_list(my_list, 5, 9))  # Out of range
print(my_list)  # Original remains unchanged
