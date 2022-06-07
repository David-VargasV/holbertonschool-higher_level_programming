#!/usr/bin/python3

'''
Write a function that returns True if the object is an instance
of a class that inherited from the specified class.
'''


def inherits_from(obj, a_class):
    '''Function that returns True or False'''
    return isinstance(obj, a_class) and type(obj) is not a_class

