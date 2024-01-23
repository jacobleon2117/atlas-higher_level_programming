#!/usr/bin/python3

"""
Module containing the function then returns a list of all of the
methods of the object class passed as a parameter
"""


def lookup(obj):
    """
    lookup function accepts an object (e.g list, int, string) as a paramater
    then returns a list of all of the methods that object has

    Args:
        obj: the object type to retrieve the methods of
    """

    method_list = []
    for method in dir(obj):
        method_list.append(method)
    return method_list