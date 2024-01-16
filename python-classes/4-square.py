#!/usr/bin/python3

"""
This module defines a class Square with an attribute size.
"""


class Square:
    """
    The Square class with a size attribute.
    """
    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
        size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter for size attribute.
        """
        return self.__size
