#!/usr/bin/python3
"""Defines a function for converting a Python class instance to a JSON-compatible dictionary."""


def class_to_json(obj):
    """Return the dictionary representation of a Python class instance.

    Args:
        obj: A Python class instance.

    Returns:
        dict: A dictionary representation of the class instance.
    """
    return obj.__dict__
