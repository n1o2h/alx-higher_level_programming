#!/usr/bin/python3
"""save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write to a txt file using json format
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
