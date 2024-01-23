#!/usr/bin/python3

"""
Module containing function to write content to a file and overwrite as needed
"""
import json


def save_to_json_file(object, filename):
    """
    Save content to a file as a JSON object

    Args:
        filename: Name of the file.
        object: the content being saved as JSON
    """

    with open(filename, 'w') as file:
        file.write(json.dumps(object))