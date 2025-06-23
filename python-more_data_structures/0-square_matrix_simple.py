#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with squared values
    return [[num ** 2 for num in row] for row in matrix]
