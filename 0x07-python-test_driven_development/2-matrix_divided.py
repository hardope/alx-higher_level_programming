#!/usr/bin/python3
"""Matrix division"""


def matrix_divided(matrix, div):
    """Divides every element of a matrix
    Args:
        matrix (list): A list of lists of integers
        or floats div (int/float): The divisor.
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError(
            "Each row of the matrix must have the same size")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    new_matrix = [[eval("{:.2f}".format(num / div)) for num in row]
                  for row in matrix]
    return new_matrix
