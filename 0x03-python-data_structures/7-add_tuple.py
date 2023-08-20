#!/usr/bin/python3

"""function that adds 2 tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples and returns a new tuple"""

    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0, 0) if len(tuple_a) == 1 else (0, 0)
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0) if len(tuple_b) == 1 else (0, 0)

    new_tuple = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    print(f"Tuple A:{tuple_a}")
    print(f"Tuple B:{tuple_b}")
    return new_tuple
