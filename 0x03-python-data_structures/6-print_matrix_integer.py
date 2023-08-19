#!/usr/bin/python3

"""print a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    """print a matrix of integers"""
    for row in matrix:
        for col_idx in row:
            print("{:d}".format(col_idx), end='')
            if col_idx < len(row):
                print(" ", end="")
        print()
