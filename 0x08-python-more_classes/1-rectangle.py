#!/usr/bin/python3


""" Define a class"""


class Rectangle:
    """rectangle representation"""
    def __init__(self, width=0, height=0):
        """initialise width, height

            Args:
                width(int), height(int)
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the width"""
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value
