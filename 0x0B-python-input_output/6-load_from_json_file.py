#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a python object from JSON"""
    with open(filename) as a_file:
        return json.load(a_file)
