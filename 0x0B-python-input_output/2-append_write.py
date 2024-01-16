#!/usr/bin/python3
""" append_write function """


def append_write(filename="", text=""):
    """
    Add a string to the end of a text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
