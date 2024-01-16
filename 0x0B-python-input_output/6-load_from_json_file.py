#!/usr/bin/python3
"""load_from_json_file function"""

import json


def load_from_json_file(filename):
    """
    make a python file from a json file
    """

    with open(filename) as file:
        return json.load(file)
