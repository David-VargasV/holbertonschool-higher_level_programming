#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []

    for n in range(list_length):
        try:
            tmp = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            tmp = 0
        except ZeroDivisionError:
            print("division by 0")
            tmp = 0
        except IndexError:
            print("out of range")
            tmp = 0
        finally:
            n_list.append(tmp)
    return (n_list)
