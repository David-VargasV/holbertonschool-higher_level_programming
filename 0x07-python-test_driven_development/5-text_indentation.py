#!/usr/bin/python3
"""
Text indentation

Function that prints a text
"""


def text_indentation(text):

    """
    function that prints a text with
    2 new lines after each of these characters: ., ? and :
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    sign = 0
    for x in text:
        if sign == 0:
            if x == " ":
                continue
            else:
                sign = 1
        if sign == 1:
            if x == "." or x == "?" or x == ":":
                print(x)
                print()
                sign = 0
            else:
                print(x, end="")
