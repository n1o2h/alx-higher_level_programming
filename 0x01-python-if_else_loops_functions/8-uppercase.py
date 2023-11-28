#!/usr/bin/python3
def uppercase(str):
    for x in str[:]:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            char = chr(ord(x) - ord('a') + ord('A'))
        else:
            char = x
        print("{}".format(char), end="")
    print()
