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

    def to_json(self):
        """Get a dictionary representation"""
        return self.__dict__
