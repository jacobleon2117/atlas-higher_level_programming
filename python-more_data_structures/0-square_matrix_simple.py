#!/usr/bin/python3
def spr(i):
    square = i * i
    return square

def  square_matrix_simple(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(spr, matrix[i])))
        return new_matrix