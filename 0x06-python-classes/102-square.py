#!/usr/bin/python3
"""Square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """
        initialize a new instance
        Attribute:
        - size (int): the size of the square
        """
        self.size = size

    # Getter methode for the size
    @property
    def size(self):
        return self.__size

    # Setter methode for the size
    @size.setter
    def size(self, value):
        # size must be an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # size must be positive
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # returns the current square area
    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __nq__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return False

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
