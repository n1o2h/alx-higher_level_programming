#!/usr/bin/python3
""" module documentation """


def inherits_from(obj, a_class):
    """ a function that returns True or false"""
    return not (not isinstance(obj, a_class) or type(obj) == a_class)
