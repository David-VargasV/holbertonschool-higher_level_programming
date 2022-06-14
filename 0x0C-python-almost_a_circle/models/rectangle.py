#!/usr/bin/python3
'''Write the class Rectangle'''


import re
from models.base import Base


class Rectangle(Base):
    '''Initialize class that inherits Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' returns the area value'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        print("\n" * self.y +
              (" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def __str__(self):
        '''return str'''
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if len(args):
            for p, arg in enumerate(args):
                if p == 0:
                    self.id = arg
                elif p == 1:
                    self.width = arg
                elif p == 2:
                    self.height = arg
                elif p == 3:
                    self.x = arg
                elif p == 4:
                    self.y = arg

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        return {
            "id": self.id,
            "widht": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
