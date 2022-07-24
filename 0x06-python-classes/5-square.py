#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialises a new square"""

        self.__size = size

    @property
    def size(self):
        """str: The size of the current square"""
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("sie must be >= 0")

        self.__size = value

    def area(self):
        return self.__size * self.__size

    def 
