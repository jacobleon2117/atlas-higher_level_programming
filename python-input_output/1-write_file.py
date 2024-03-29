#!/usr/bin/python3

"""
module containing function to write content to a file and overwrite as needed
"""


def write_file(filename="", content=""):
    """
    Write content to a specified file

    Args:
        filename: Name of the file. Created if it doesn't exist
        content: the content to write to filename
    """

    with open(filename, 'w') as file:
        file.write(content)
    return len(content)