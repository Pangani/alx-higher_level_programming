#!/usr/bin/python3


""" size validation """


class Square:
    """representation of a square"""
    def __init__(self, size=0):
        """initialise size

            Args:
                size(int)
        """
        self.__size = size

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
