#!/usr/bin/python3
from sys import argv
sum = 0
if __name__ == "__main__":
    for x in range(1, len(argv)):
        sum += int(argv[x])
    print("{}".format(sum))
