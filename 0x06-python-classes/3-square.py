#!/usr/bin/python3
"""defines a square"""


class Square:
    """create a class"""
    def __init__(self, size=0):
        """constructor"""
        self.__size = size
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    """calculate the square's area"""
    def area(self):
        return (self.__size * self.__size)
