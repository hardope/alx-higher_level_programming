#!/usr/bin/python3
"""This program create a new int called MyInt and is rebel!!!"""


class MyInt(int):
    """Class MyInt is like an int but Rebel"""

    def __eq__(self, other_num):
        """Rebel!!! equal is not equal"""
        return super().__ne__(other_num)

    def __ne__(self, other_num):
        """Rebel!!! not equal is equal"""
        return super().__eq__(other_num)
