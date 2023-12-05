#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    y = my_list[0]
    for x in my_list:
        y = x if x > y else y
    return y
