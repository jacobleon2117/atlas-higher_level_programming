#!/usr/bin/python3

"""
Module that defines a class square with an attribute size.
"""


class square:
    """
    Square class with an attribute.
    """
    def __init__(self, size=0):
        """
        Constructor for the square class.
        
        Parameters:
        size (int): Size of the square.
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.size = size