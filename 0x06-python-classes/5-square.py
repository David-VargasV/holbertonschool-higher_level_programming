#!/usr/bin/python3

"""Class Square that defines a square"""


class Square:
    """Initialize square with error messages - based on 4-square.py"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size**2)

    def my_print(self):
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
