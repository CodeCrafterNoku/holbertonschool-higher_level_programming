#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Print the dictionary by ordered keys
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
