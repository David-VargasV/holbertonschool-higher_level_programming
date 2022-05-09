#!/usr/bin/env python3
def no_c(my_string):
    n_str = ""
    for l in my_string:
        if not (l == 'c' or l == 'C'):
            n_str += l
    return n_str
