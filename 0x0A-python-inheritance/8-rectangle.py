#!/usr/bin/python3

'''Write a class Rectangle that inherits from (based on 7-base_geometry.py)'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Initialize the class Rectangle'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
