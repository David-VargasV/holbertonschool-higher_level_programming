#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list[:]
    for x in range(len(n_list)):
        if n_list[x] == search:
            n_list[x] = replace
    return n_list
