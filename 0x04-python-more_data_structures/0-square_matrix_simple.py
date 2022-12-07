#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for i in matrix:
        tmp = []
        for j in i:
            tmp.append(j * j)
        matrix_2.append(tmp)
    return matrix_2
