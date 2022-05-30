#!/usr/bin/python3
"""
Print square

Function that prints a square with the character #
"""


def print_square(size):

    """The function that defines the size of the square"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size)
