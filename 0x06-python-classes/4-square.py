#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initializes a new square

        Args:
            size (int): The size of a square
        """

        self.__size = size

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculate the area of current square.

        Return:
            The current square area.
        """

        return self.__size * self.__size
