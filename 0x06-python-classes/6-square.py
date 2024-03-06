#!/usr/bin/python3
"""defines a square"""


class Square:
    """create a class"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor"""
        self.__size = size
        self.__position = position
    """calculate the square's area"""
    def area(self):
        return (self.__size * self.__size)

    @property
    def position(self):
        """get the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set the position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for j in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end='')
                for n in range(0, self.__size):
                    print("#", end='')
                print("")
