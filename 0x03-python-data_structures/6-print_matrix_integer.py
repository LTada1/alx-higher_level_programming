#!/usr/bin/python3i
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
    # for i in range(len(matrix)):
    # for j in range(len(matrix[i])):
    # print(matrix[i][j], end='')
    # if i == matrix[0][]
    # print()
