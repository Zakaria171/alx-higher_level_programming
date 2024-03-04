#!/usr/bin/python3
"""defines a square"""


class Square:
    """create a class"""
    def __init__(self, size=0):
        """constructor"""
        self.__size = size
    """calculate the square's area"""
    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        """get the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
