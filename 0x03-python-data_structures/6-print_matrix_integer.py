#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = matrix

    for line in a:
        print(' '.join(map(str, line)))
