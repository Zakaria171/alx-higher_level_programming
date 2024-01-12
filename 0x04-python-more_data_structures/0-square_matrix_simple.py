#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])
    sqr_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sqr_matrix[i][j] = matrix[i][j] **2
    return (sqr_matrix)
