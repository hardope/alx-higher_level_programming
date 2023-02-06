#!/usr/bin/python3
"""
This program take a file and read it, search a string
and add other string on the next line
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Open and reads a file, search a string in all the file.
    and after each ocurrence add other string (new_string)
    Args:
    - filename: string
    - search_string: string
    - new_string: string
    """

    with open(filename, mode="r+", encoding="utf-8") as _file:
        all_text = _file.readlines()
        new_text = ""

        for line in all_text:
            new_text += line
            if (search_string in line):
                new_text += new_string

        # This method position the cursor to the beginning of the file
        _file.seek(0)
        _file.write(new_text)
