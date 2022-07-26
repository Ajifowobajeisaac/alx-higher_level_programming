#!/usr/bin/python3

"""A class that defines a square"""


class Sqaure:
    """Represents a square"""

    def __init__(self, size=0, postition=(0, 0)):
        """Initialises a new square"""

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: The size of the current square"""

        return self.__size
 
    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0 :
            raise ValueError("size musst be >= 0")

        self.__size = value

    @property
    def position(self):
        """tuple: The position of the square"""

        return self.__position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple):
            raise TypeError("position must be tuple of 2 positive integers")
