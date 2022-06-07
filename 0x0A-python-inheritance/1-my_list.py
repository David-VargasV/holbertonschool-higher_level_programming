#!/usr/bin/python3

'''Class MyList that inherits from list'''


class MyList(list):
    '''Initialize the class'''
    def print_sorted(self):
        print(sorted(self))
