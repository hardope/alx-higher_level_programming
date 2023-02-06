#!/usr/bin/python3
"""Text indentations"""


def text_indentation(text):
    """Prints a text with 2 new lines
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    special = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be string")
    for x in text:
        print(x, end='')
        if x in special:
            print('\n\n', end='')
