#!/usr/bin/python3
"""
This program reads files .json and convert to types of python
"""


import json


def load_from_json_file(filename):
    """
    Read a file and convert the content (JSON) to python types
    Args:
      - filename: path
    """

    with open(filename, mode="r", encoding="utf-8") as _file:
        return (json.loads(_file.read()))
