from numpy import *
from sympy import *

import matplotlib.pyplot as plt

def central_difference(function, x, h=1.0E-4):
    # the function to approximate the value of the derivative / gradient
    return (function(x + h) - function(x - h)) / (2 * h)

def forward_difference(function, x, h=1.0E-4):
    # the function to approximate the value of the derivative / gradient
    return (function(x + h) - function(x)) / (h)

def backward_difference(function, x, h=1.0E-4):
    # the function to approximate the value of the derivative / gradient
    return (function(x) - function(x - h)) / (h)

def print_matrix(mat):
    for i in range(len(mat)):
        print(mat[i])

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
yResult[1] = 1.580645161       # 1.86465
yResult[2] = 1.932258065       # 2.38344
yResult[-1] = 1.5

for i in range(iteration):
    yVals.append(symbols(('y' + str(i))))
    eVals.append(exp(i * -2))

matrix = [ [] for i in range(iteration) ]
for i in range(iteration):
    matrix[i] = [ 0 for i in range(iteration) ]

matrix[0][0] = 1 #16
# matrix[0][1] = 0 #-40
# matrix[0][2] = 0 #25

for i in range(iteration - 2):
    matrix[i + 1][i + 0] = 20
    matrix[i + 1][i + 1] = -49
    matrix[i + 1][i + 2] = 30

# matrix[-1][-3] = 25
# matrix[-1][-2] = -30
matrix[-1][-1] = 1 #31

for i in range(3, 11):
    yResult[i] = (float(eVals[i - 1]) - (20 * yResult[i - 2]) - (-49 * yResult[i - 1])) / 30

# yResult[-1] = (float(eVals[-1]) - (25 * yResult[i - 2]) - (-30 * yResult[i - 1])) / 31

print_matrix_appended(matrix, yVals, eVals)

# plt.scatter(arange(0, 2.1, 0.2), yResult)

# print(yResult)

# plt.show()