#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """Multiplies two matricies
    """

    # check if the two matrix's aren't empty
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    # check the validity of the content of each elemtent
    # for matrix a
    if not all(type(row) == list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    # check the validity of the content of each elemtent
    # for matrix b
    if not all(type(row) == list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Check the validity of the content of each list
    # inside each list of matrix a
    row_len = len(m_a[0])
    if not all(len(row) == row_len for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(type(num) in [int, float] for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    # Check the validity of the content of each list
    # inside each list of matrix a
    row_len = len(m_b[0])
    if not all(len(row) == row_len for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if not all(type(num) in [int, float] for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    # check if the two vectors are multipliable
    acols = len(m_a[0])
    arows = len(m_a)
    brows = len(m_b)
    bcols = len(m_b[0])
    if acols != brows:
        raise ValueError("m_a and m_b can't be multiplied")

    product = [[0 for x in range(bcols)] for y in range(arows)]
    for row_i in range(len(m_a)):
        col_b = 0
        while (col_b < bcols):
            sum_t = 0
            for col_i in range(len(m_a[row_i])):
                sum_t += m_a[row_i][col_i] * m_b[col_i][col_b]
            product[row_i][col_b] = sum_t
            col_b += 1
    return product
