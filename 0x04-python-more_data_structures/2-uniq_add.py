#!/usr/bin/python3
def uniq_add(my_list=[]):
    uq_set = set(my_list)
    sum_n = 0
    for x in uq_set:
        sum_n += x
    return sum_n
