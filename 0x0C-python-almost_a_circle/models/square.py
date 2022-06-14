#!/usr/bin/python3
'''Write the class Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''''Initialize class that inherits Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if len(args):
            for p, arg in enumerate(args):
                if p == 0:
                    self.id = arg
                elif p == 1:
                    self.size = arg
                elif p == 2:
                    self.x = arg
                elif p == 3:
                    self.y = arg

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y,
                }
