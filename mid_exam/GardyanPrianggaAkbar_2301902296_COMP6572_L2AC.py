from math import pi

import matplotlib.pyplot as py
import sympy as sp
import numpy as np
import time


x = sp.Symbol('x')
y = sp.Symbol('y')
n = sp.Symbol('n')

#No 1
#a
#X for tools and equipment
#Y for materials for EACH cloth
revenueEq = (1.5*x + 2*x)*(n/2)
totalCostEq = y + x*n
profitEq = revenueEq - totalCostEq
#I will be assuming Y has the value of 1000X and X has the value of 200000
xVal = 200000
yVal = 50*xVal
print("a. Total cost:", totalCostEq)
print("   Revenue:", revenueEq)
temp = 1
while (revenueEq.evalf(subs={x : xVal, y: yVal, n  : temp}) <= totalCostEq.evalf(subs={x : xVal, y: yVal, n: temp})):
    temp+=1
print("The solution means that once", temp, "clothes is sold, we will have broken even between cost and revenue. So any amount of clothes after this will produce a profit.")
#b
nVal = temp+1
print("b. For", nVal, "amount of clothes, he will get a profit of Rp", profitEq.evalf(subs={x: xVal, y: yVal, n:nVal}))
#c
nVals = [i for i in range(500, 500*10, 100)]
profits = []
for nval in nVals:
    profits.append(profitEq.evalf(subs={x: xVal, y: yVal, n:nval}))
py.plot(nVals, profits)
py.xlabel("Number of clothes")
py.ylabel("Profits")
py.show()
#d
#LU Decomposition
matrix = [[1, 2, 3, 10], 
          [4, 7, 5, 4], 
          [7, 1, 9, 11]]
intervals = []
start = time.time()
sp.solve_linear_system_LU(sp.Matrix(matrix), [x, y, n])
end = time.time()
intervals.append(end - start)
#Gauss Elimination
#According to SymPy, Gauss Elimination is more efficient than Gauss-Jordan elimination
start = time.time()
sp.solve_linear_system(sp.Matrix(matrix), x, y, n)
end = time.time()
intervals.append(end - start)
print("d.")
print("LU Decomposition (time taken):", intervals[0])
print("Gauss Elimination (time taken):", intervals[1])
print()

#No 2
#a
functionOri = (x-1)
function = functionOri
def no_2_eq(function, n, xVal):
    answer = 0
    for i in range(1, n+1):
        if (i == 1):
            answer = function.evalf(subs={x: xVal})
        elif (i % 2 == 1): #Odd
            answer = answer + (functionOri**i/i).evalf(subs={x: xVal})
        else:
            answer = answer - (functionOri**i/i).evalf(subs={x: xVal})
    return answer
print("No 2:")
actualFunc = sp.ln(x)
xVal = 2
trueError = actualFunc.evalf(subs={x: 2}) - no_2_eq(function, 5, xVal)
print("a. True Error:", trueError)
#b
absError = abs(trueError)
target = 0.0001
actualVal = actualFunc.evalf(subs={x: 2})
answer = -500
temp = 1
while (abs(actualVal - answer) >= target):
    if (temp == 1):
        answer = function.evalf(subs={x: xVal})
    elif (temp % 2 == 1): #Odd
        answer = answer + (functionOri**temp/temp).evalf(subs={x: xVal})
    else:
        answer = answer - (functionOri**temp/temp).evalf(subs={x: xVal})
    temp += 1
print("b.", temp-1)
#c
target = 0.1/100
answer = -99999999999999999
temp = 1
while ((abs(actualVal - answer)/actualVal) >= target):
    if (temp == 1):
        answer = function.evalf(subs={x: xVal})
    elif (temp % 2 == 1): #Odd
        answer = answer + (functionOri**temp/temp).evalf(subs={x: xVal})
    else:
        answer = answer - (functionOri**temp/temp).evalf(subs={x: xVal})
    temp += 1
print("c.", temp-1)
#d
answers = []
for n in range(1, 11):
    answers.append(abs(actualVal - no_2_eq(function, n, xVal)))
xValues = [x for x in range(1, 11)]
py.plot(np.array(xValues), np.array(answers))
py.xlabel("Terms number")
py.ylabel("Approximate error")
py.show()
print()

#No 3
def simpson_rule(equation, a, b, n):
    """
    Method to get the integration approximation of a function using simpson rule
    
    Parameters:
    equation: The equation f(x)
    a: lower bound of the integral
    b: upper bound of the integral
    n: no of segments
    """
    
    h = (b-a)/n
    x = sp.Symbol('x')
    xVal = a
    
    result = 0
    #First segment
    result += equation.evalf(subs={x:xVal})
    xVal += h
    #Other segments
    for i in range(1, n+1):
        if (i == n):  #If last segment
            result += equation.evalf(subs={x:xVal})
        else:
            if (i % 2 != 0):
                result += equation.evalf(subs={x:xVal}) * 4
            else:
                result += equation.evalf(subs={x:xVal}) * 2
        xVal += h
    
    result *= h/3
    
    return result

function = sp.sin(x)

answers = []
for n in range(4, 11, 2):
    answers.append(simpson_rule(function, 0, pi, n))

print("No 3:")
n = 4
for i in range(len(answers)):
    print("N is", n, ":", answers[i])
    n+=2    #Simpson only accepts even segments