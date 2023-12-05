#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for j in range(len(x)):
            if j < len(x) - 1:
                print("{:d}".format(x[j]), end=" ")
            else:
                print("{:d}".format(x[j]), end="")
        print()
