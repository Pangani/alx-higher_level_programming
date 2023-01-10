#!/usr/bin/python3


""" size validation """


class Square:
    """representation of a square"""
    def __init__(self, size=0):
        """initialise size

            Args:
                size(int)
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
