#!/usr/bin/python3
"""Module containing the function append_write"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
