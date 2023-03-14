#!/usr/bin/python3
"""
This program takes two matrices and multiply them with the library numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Takes two matrices and multiply them with numpy
      Args:
        m_a: list of lists (int or float)
        m_b: list of lists (int or float)
    """
    return np.matmul(m_a, m_b)
