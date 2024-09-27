#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to rotate 90 degrees clockwise
    for row in matrix:
        row.reverse()
