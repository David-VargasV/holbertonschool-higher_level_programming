#!/usr/bin/python3

'''
Write a function that creates an Object from a “JSON file”:
'''

import json


def load_from_json_file(filename):
    '''Function that create an object'''
    with open(filename, 'r') as f:
        return json.load(f)
