#!/usr/bin/python3
"""Defines a file-appending"""


def append_write(filename="", text=""):
    """Appends a string to the end
    Args:
        filename: name of file to append to
        text: string to append to file
    Return:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
