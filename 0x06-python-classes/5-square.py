#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialises a new square"""

        self.__size = size

    @property
    def size(self):
        """int: The size of the current square"""
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """int: The area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints '#' based on the size"""

        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
