#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for x in range(len(my_list)):
        new_list[x] = replace if new_list[x] == search else new_list[x]
    return new_list
