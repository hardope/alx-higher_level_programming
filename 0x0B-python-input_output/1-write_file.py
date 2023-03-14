#!/usr/bin/python3
"""
This program writes in a file if doesn't exists create the file
"""


def write_file(filename="", text=""):
    """
    Write in a file, if doesn't exists create the file
    Args:
      - filename: string
      - text: string
    """

    with open(filename, mode="w", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))
