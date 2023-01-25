#!/usr/bin/python3
"""Defines student class module"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initialise the new student
        Args:
            first_name: first name of new student
            last_name: last name of new student
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation"""
        if (type(attrs) == list and 
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
