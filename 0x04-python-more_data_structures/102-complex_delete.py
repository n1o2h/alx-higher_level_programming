#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dict = a_dictionary.copy()
    for key, val in a_dict.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
