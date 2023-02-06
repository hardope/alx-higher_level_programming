#!/usr/bin/python3
"""
This program can append text in a file,
create the file if doesn't exists
"""


def append_write(filename="", text=""):
    """
    Append text to the end of file, and created if doesn't exists.
    Args:
      - filename: string
      - text: string
    """

    with open(filename, mode="a", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))
