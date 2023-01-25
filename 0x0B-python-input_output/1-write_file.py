#!/usr/bin/python3
"""Defines Writing to file function"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file

    Args:
        filename (str): The name of the file
        text (str): The text to write to file
    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
