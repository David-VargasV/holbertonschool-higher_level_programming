#!/usr/bin/python3
'''Write the class Base'''


from fileinput import filename
import json


class Base:
    '''Initialize the class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                l_dic = [x.to_dictionary() for x in list_objs]
                file.write(Base.to_json_string(l_dic))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                l_dic = Base.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in l_dic]
        except Exception:
            return []
