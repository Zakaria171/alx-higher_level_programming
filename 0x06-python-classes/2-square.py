#!/usr/bin/python3
"""defines a square"""


class Square:
    """create a class"""
    def __init__(self, size=0):
        """constructor"""
        self.__size = size
        if (isinstance(size, int) is False):
            print("size must be an integer")
        elif size < 0:
            print("size must be >= 0")
