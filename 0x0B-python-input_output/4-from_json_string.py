#!/usr/bin/python3
"""
This program converts JSON to dictionaries
"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON stringx
    Args:
      - my_str: str
    """
    return (json.loads(my_str))
