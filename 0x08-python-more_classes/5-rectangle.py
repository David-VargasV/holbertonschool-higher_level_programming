#!/usr/bin/python3

"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Initialize the Rectangle with, width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the Rectangle area"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns the Rectangle perimeter"""
        if (self.width == 0 or self.height == 0):
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Print the rectangle with the character #"""
        n = ""
        if (self.width == 0 or self.height == 0):
            return n
        else:
            for x in range(self.height):
                if x == self.height - 1:
                    n += self.width * "#"
                else:
                    n += self.width * "#" + "\n"
            return n

    def __repr__(self):
        """Returns the string representation of Rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Print the message"""
        print("Bye rectangle...")
