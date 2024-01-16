#!/usr/bin/python3
""" write_file function """


def write_file(filename="", text=""):
    """
    write a str to a txt file
    Args:
        filename: file name
        text: txt to write in file
    """

    with open(filename, mode="w", encoding="UTF-8") as file:
        return file.write(text)
