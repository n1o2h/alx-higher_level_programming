#!/usr/bin/python3
""" importing Base class """
from models.base import Base


class Rectangle(Base):
    """ new class that inherits from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ a public method that calculate the area"""
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for _ in range(self.y):
            print()
        for x in range(self.height):
            print(" " * self.x + "#" * self.__width)

    def update(self, *args):
        """ a function that assigns an argument to each attribute"""
        for x in range(len(args)):
            if x == 1:
                arg = args[x]
                self.width = arg
            if x == 2:
                arg = args[x]
                self.height = arg
            if x == 3:
                arg = args[x]
                self.x = arg
            if x == 4:
                arg = args[x]
                self.y = arg
            if x == 0:
                arg = args[x]
                self.id = arg

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}" \
                f" - {self.width}/{self.height}"
