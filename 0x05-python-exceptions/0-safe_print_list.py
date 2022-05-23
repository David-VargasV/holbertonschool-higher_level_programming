#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tmp = 0
    for y in my_list[:x]:
        try:
            print(y, end="")
            tmp = tmp + 1
        except IndexError:
            break
    print()
    return tmp
