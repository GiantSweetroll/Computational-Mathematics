from numpy import *
from sympy import *
import sympy as sp

import matplotlib.pyplot as plt

def central_difference(function, x, h=1.0E-4):
    return (function(x + h) - function(x - h)) / (2 * h)

def forward_difference(function, x, h=1.0E-4):
    return (function(x + h) - function(x)) / (h)

def backward_difference(function, x, h=1.0E-4):
    return (function(x) - function(x - h)) / (h)

def print_matrix(mat):
    for m in mat:
        print(m)

def print_matrix_appended(mat, yVector, result):
    for i in range(len(mat)):
        print((mat[i]), end="   ")
        print("[" , yVector[i] , "]", end="   ")
        print("[" , float(result[i]) , "]")

iteration = 11

yVals = []
eVals = []

yResult = [ 0 for i in range(iteration)]
yResult[0] = 1
yResult[-1] = 1.5

for i in range(iteration):
    yVals.append(symbols(('y' + str(i))))
    eVals.append(exp(i * -2))

matrix = []
for i in range(iteration):
    matrix.append([ 0 for i in range(iteration) ])

matrix[0][0] = 1

for i in range(iteration - 2):
    matrix[i + 1][i + 0] = 20
    matrix[i + 1][i + 1] = -49
    matrix[i + 1][i + 2] = 30

matrix[-1][-1] = 1

for i in range(3, 11):
    yResult[i] = (float(eVals[i - 1]) - (20 * yResult[i - 2]) - (-49 * yResult[i - 1])) / 30

print_matrix_appended(matrix, yVals, eVals)

# yVars = sp.symbols('y_0 y_1 y_2 y_3 y_4 y_5 y_6 y_7 y_8 y_9 y_10')
# for i in range(len(matrix)):
#     matrix.append(eVals[i])
# 
# m = sp.Matrix(matrix)
# result = sp.solve_linear_system_LU(m, yVars)