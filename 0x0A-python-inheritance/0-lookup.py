#!/usr/bin/python3
""" module documentation"""


def lookup(obj):
    """a function that returns the list of available attributes and methods"""
    return [attr for attr in dir(obj)]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-lookup.txt")
