#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """check if an object is an inherited instance.

    Args:
        obj(any): The object to check
        a_class type: The class to match the type of obj
    Returns:
        if obj is an inherited instance of a_class - True
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
