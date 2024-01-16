#!/usr/bin/python3

"""
This module that defines a class square with an attribute size.
"""


class square:
    """
    The square class with an attribute.
    """
    def __init__(self, size=0):
        """
        The constructor for the square class.
        
        Parameters:
        size (int): Size of the square.
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.size = size

def area(self):
    """
    Method of the square class that finds the area.

    Return:
        the area of the sqaure.
    """
    return self.__size * self.__size
        