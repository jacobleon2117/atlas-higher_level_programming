#!/usr/bin/python3

"""
Module containing a function that reads the contents of a file
"""
import json


def load_from_json_file(filename=""):
    """
    read_file opens a file, reads its contents, and prints those contents
    """

    with open(filename, 'r') as file:
        json_obj = json.loads(file.read())
    return json_obj