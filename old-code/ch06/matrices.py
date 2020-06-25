from vectors import *
from random import randint

# def multiply_matrix_vector(matrix, vector):
#     return linear_combination(vector, *zip(*matrix))

# def multiply_matrix_vector(matrix,vector):
#     return tuple(
#         sum(vector_entry * matrix_entry
#             for vector_entry, matrix_entry in zip(row,vector))
#         for row in matrix
#     )

def multiply_matrix_vector(matrix,vector):
    return tuple(
        dot(row,vector)
        for row in matrix
    )

def matrix_multiply(a,b):
    return tuple(
        tuple(dot(row,col) for col in zip(*b))
        for row in a
    )

def random_matrix(rows,cols,min=-2,max=2):
    return tuple(
        tuple(
        randint(min,max) for j in range(0,cols))
        for i in range(0,rows)
    )

def to_latex(m):
    return '\\'.join("&".join(str(cell) for cell in row) for row in m)

def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i==j else 0 for j in range(1,n+1))
    standard_basis = [standard_basis_vector(i) for i in range(1,n+1)]
    cols = [transformation(v) for v in standard_basis]
    return tuple(zip(*cols))

def transpose(matrix):
    return tuple(zip(*matrix))

def matrix_power(power,matrix):
    result = matrix
    for _ in range(1,power):
        result = matrix_multiply(result,matrix)
    return result
