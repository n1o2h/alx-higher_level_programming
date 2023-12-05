#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        xa, ya = 0, 0
    elif len(tuple_a) == 1:
        xa, ya = tuple_a[0], 0
    else:
        xa, ya = tuple_a[0], tuple_a[1]
    if len(tuple_b) == 0:
        xb, yb = 0, 0
    elif len(tuple_b) == 1:
        xb, yb = tuple_b[0], 0
    else:
        xb, yb = tuple_b[0], tuple_b[1]
    return xa + xb, ya + yb
