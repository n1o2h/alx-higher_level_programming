#!/usr/bin/python3
"""
from_json_string function
"""


import json


def from_json_string(my_str):
    """ Returns python representation of a json str """
    return json.loads(my_str)
