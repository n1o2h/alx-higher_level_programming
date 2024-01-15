#!/usr/bin/python3
"""Square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize a new instance
        Attribute:
        - size (int): the size of the square
        """
        self.size = size
        self.position = position

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

    # Getter methode for the position
    @property
    def position(self):
        return self.__position

    # Setter methode for the position
    @position.setter
    def position(self, value):
        if ((not isinstance(value, tuple)) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not all(isinstance(x, int) for x in value)
                or not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # returns the current square area
    def area(self):
        return self.__size ** 2

    # Print the square with the character '#'
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
