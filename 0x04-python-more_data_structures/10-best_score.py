#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        n_dic = [(value, key) for key, value in a_dictionary.items()]
        return(max(n_dic)[1])
