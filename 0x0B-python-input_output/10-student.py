#!/usr/bin/python3

'''
Write a class Student that defines a student by:
(based on 9-student.py)
'''


class Student:
    '''Initialize the class'''
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Public method'''

        n_dic = {}
        if attrs is None:
            return self.__dict__
        for x in attrs:
            if hasattr(self, x):
                n_dic[x] = getattr(self, x)
        return n_dic
