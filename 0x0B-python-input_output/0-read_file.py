#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """read file with open()"""
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
