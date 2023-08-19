#!/usr/bin/python3

"""function that adds 2 tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples and returns 2 integers"""

    if len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) < 2:
            if len(tuple_a) == 0:
                new_tuple = (0 + tuple_b[0]), (0 + tuple_b[1])
            elif len(tuple_a) == 1:
                new_tuple = (tuple_a + tuple_b[0]), (0 + tuple_b[1])
        elif len(tuple_b) < 2:
            if len(tuple_b) == 0:
                new_tuple = (tuple_a[0] + 0), (tuple_a[1] + 0)
            elif len(tuple_b) == 1:
                new_tuple = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0)
    elif len(tuple_a) and len(tuple_b) < 2:
        new_tuple = (tuple_a[0] + tuple_b[0]), (0 + 0)
    else:
        new_tuple = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    return new_tuple
