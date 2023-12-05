#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = [my_list[x] % 2 - 1 for x in range(len(my_list))]
    return result
