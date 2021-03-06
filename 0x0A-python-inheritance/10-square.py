#!/usr/bin/python3

'''Write a class Square that inherits from Rectangle (9-rectangle.py)'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Initialize the class Square'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size**2)
