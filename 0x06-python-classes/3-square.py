#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initializes a new square"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of square

        Returns:
            The current square area
        """

        return self.__size * self.__size
