#!/usr/bin/python3
""" square module """


class Rectangle:
    """ A rectangle class """

    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ initiate width and height """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width * self.__height == 0:
            return 0
        return (2 * self.__height + 2 * self.__width)

    def __str__(self):
        if self.__width * self.__height == 0:
            return ""
        s = ""
        for i in range(self.__height):
            if i:
                s += '\n'
            s += self.__width * "#"
        return s

    def __repr__(self):
        if self.__width * self.__height == 0:
            return ""
        x = f'<{self.__module__}.{self.__class__.__name__}'
        x += f' object at {hex(id(self))}>'
        return x
