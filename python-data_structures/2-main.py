#!/usr/bin/python3
replace_in_list = __import__("2-replace_in_list").replace_in_list

my_list = [1, 2, 3, 4, 5]
print(replace_in_list(my_list, 3, 9))  # Valid
print(replace_in_list(my_list, -1, 9))  # Negative
print(replace_in_list(my_list, 5, 9))  # Out of range
print(my_list)  # Show original list was modified
