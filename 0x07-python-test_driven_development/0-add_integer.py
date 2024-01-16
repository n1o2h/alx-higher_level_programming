#!/usr/bin/python3
"""
This is module documontation
"""

def add_integer(a, b=98):
    """
    Return the addition of a and b.

    Args:
        a: the first value.
        b: the second value.
    """
    if type(a) in [int, float]:
        try:
            a = int(a)
        except:
            raise TypeError('a most be an integer')
    else:
        raise TypeError('a most be an integer')

    if type(b) in [int, float]:
        try:
            b = int(b)
        except:
            raise TypeError('b most be an integer')
    else:
        raise TypeError('b most be an integer')

    return a + b
