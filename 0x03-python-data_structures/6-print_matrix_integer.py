#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        for j in range(len(i)):
            if i[j + 1] not None:
                print("{:d} ".format(j[i]), end="")
            else:
                print("{:d}".format(j[i]))
