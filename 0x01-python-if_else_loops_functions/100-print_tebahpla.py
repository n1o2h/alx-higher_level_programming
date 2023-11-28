#!/usr/bin/python3
for x in range(ord('z'), ord('a'), -2):
    print("{}{}".format(chr(x), chr(x - ord('a') + ord('A') - 1)), end="")
