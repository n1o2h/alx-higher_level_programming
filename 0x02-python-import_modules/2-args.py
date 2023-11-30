#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ctr = len(sys.argv)
    if ctr > 2:
        print("{} arguments:".format(ctr - 1))
    elif ctr == 2:
        print("{} argument:".format(ctr - 1))
    else:
        print("0 arguments.")
    for x in range(1, ctr):
        print("{}: {}".format(x, sys.argv[x]))
