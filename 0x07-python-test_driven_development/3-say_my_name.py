#!/usr/bin/python3
"""
Say my name

Function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):

    """The function that defines the names and prints a full name"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
