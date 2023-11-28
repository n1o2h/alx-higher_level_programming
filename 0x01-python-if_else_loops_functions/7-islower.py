#!/usr/bin/python3
def islower(c):
    for x in range(ord('a'), ord('z') + 1):
        if ord(c) == x:
            return True
    return False
