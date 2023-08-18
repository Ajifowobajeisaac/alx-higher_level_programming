#!/usr/bin/python3

"""print a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    """print a matrix of integers"""
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end='')
        print()
