#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for key, val in a_dictionary.items():
        if val == max(list(a_dictionary.values())):
            return key
    return None
