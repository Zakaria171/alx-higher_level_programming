#!/usr/bin/python3
"""define a Rectangle"""


class Rectangle:
    """create an empty class"""
    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """print rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ('')
        return '\n'.join("#" * self.__width for i in range(0, self.__height))

    def __repr__(self):
        """string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
