#!/usr/bin/python3
"""Defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line
    Args:
        filename: name of a file
        search_string: string where to append to after
        new_string: the strng to be appended to
    """
    text = ""
    with open(filename) as a_file:
        for line in a_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
