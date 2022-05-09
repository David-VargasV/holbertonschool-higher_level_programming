#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for letter in my_string:
        if not (letter == 'c' or letter == 'C'):
            n_str += letter
    return n_str
