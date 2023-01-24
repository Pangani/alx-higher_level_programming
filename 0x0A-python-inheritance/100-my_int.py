#!/usr/bin/python3
"""Defines a class Myint that inherits from int"""


class Myint(int):
    """Invent int operators == and !=."""

    def __eq__(self, value):
        """Override == operator with != behaviour."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with ==  behavior."""
        return self.real == value
