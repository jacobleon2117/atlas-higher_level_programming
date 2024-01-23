#!/usr/bin/python3

"""
Module containing Student class
"""


class Student:
    """
    Student class with to_json method

    Args:
        first_name: Student's first name, String
        last_name: Student's last name, String
        age: Student's age, Integer
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attr_dict = vars(self)
        if attrs is not None:
            new_dict = dict()
            for key in attrs:
                if key in attr_dict:
                    new_dict[key] = attr_dict[key]
            return new_dict
        return attr_dict

    def reload_from_json(self, json):
        attrs = vars(self)
        for key in json:
            if key in attrs:
                setattr(self, key, json[key])