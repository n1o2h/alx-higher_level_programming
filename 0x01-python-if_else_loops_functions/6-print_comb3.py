#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x != 8 or y != 9:
            print("{}{}, ".format(x, y), end="")
else:
    print("{}{}".format(x - 1, y))
