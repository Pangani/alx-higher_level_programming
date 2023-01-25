#!/usr/bin/python3
"""Defines from_json_to string function"""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
