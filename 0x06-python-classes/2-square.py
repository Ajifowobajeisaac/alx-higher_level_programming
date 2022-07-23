#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initializes a new square.

        args:
            size (int): The size of a square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
