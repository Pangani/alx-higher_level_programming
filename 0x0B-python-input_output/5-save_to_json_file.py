#!/usr/bin/python3
"""Defines a JSON file_writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object that saves text file using json"""
    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)
