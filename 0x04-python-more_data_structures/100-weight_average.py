#!/usr/bin/python3
def weight_average(my_list=[]):
    total_w = 0
    total_s = 0
    if len(my_list) == 0:
        return 0
    for x in my_list:
        score, weight = x
        total_s += score * weight
        total_w += weight
    result = total_s / total_w
    return result
