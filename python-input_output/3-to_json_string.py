#!/usr/bin/python3

"""
Mpdule containing json stringification function
"""

import json


def to_json_string(obj):
    """
    Converts provided object to JSON string
    """
    return json.dumps(obj)