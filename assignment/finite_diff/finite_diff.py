import sympy as sp
import numpy as np

def cd(f, x, xStart, h= 1.0E-4):
    df = (f.evalf(subs={x : xStart + h}) - f.evalf(subs={x : xStart - h}))/(2*h)
    return df;

def cd2(f, x, xStart, h= 1.0E-4):
    df = (f.evalf(subs={x : xStart + h}) - 2*f.evalf(subs={x : xStart}) + f.evalf(subs={x : xStart - h}))/(h**2)
    return df;

def bd(f, x, xStart, h= 1.0E-4):
    df = (f.evalf(subs={x : xStart}) - f.evalf(subs={x : xStart - h}))/(h)
    return df

def bd2(f, x, xStart, h= 1.0E-4):
    df = (f.evalf(subs={x : xStart}) - 2*f.evalf(subs={x : xStart - h}) + f.evalf(subs={x : xStart - 2*h}))/(h**2)
    return df;

def fd2(f, x, xStart, h= 1.0E-4):
    df = (f.evalf(subs={x : xStart + 2*h}) - 2*f.evalf(subs={x : xStart + h}) + f.evalf(subs={x : xStart}))/(h**2)
    return df;

def fd(f, x, xStart, h= 1.0E-4):
    df = (f.evalf(subs={x : xStart + h}) - f.evalf(subs={x : xStart}))/(h)
    return df

#Workshop
#What we know:
#y(0) = 1
#y(2) = 1.5
y = sp.Symbol('y')
x = sp.Symbol('x')
ys = sp.symbols('y_0 y_1 y_2 y_3 y_4 y_5 y_6 y_7 y_8 y_9 y_10')

df = sp.diff(y)
d2f = sp.diff(df)

eqy = d2f + 2*df + y
eqx = sp.exp(-2*x)
eqdf2 = eqx - 2*df - y
eqdf = (eqx - d2f - y)/2
eq = eqx - d2f - 2*df

sections = 10
xDelta = (2-0)/sections

iVals = []
iVals.append([1*ys[0], eqx])
for i in range(1, sections):
    sub = []
    leftHand = (ys[i+1] - 2*ys[i] - ys[i-1])/(xDelta**2)
    leftHand = leftHand + (2*ys[i+1] - ys[i])/xDelta
    leftHand = leftHand + ys[i]
    sub.append(leftHand)
    sub.append(eqx)
    iVals.append(sub)
iVals.append([1*ys[len(ys)-1], eqx])
    
#Display appended matrix
for iVal in iVals:
    print(iVal)
    
#Convert to Coefficient Matrix
cMatrix = []
#Append first row
for iVal in iVals:
    sub = []
    #append zeroes
    for i in range(sections+1):
        sub.append(0)
    
    #replace in index
    for a in iVal[0].args:
        co = a.args[0]
        print(co)
        var = a.args[1]
        index = 0
        for b in range(len(ys)):
            if (str(var) == str(ys[b])):
                index = b
                break
        
        sub[index] = co
    cMatrix.append(sub)

#Append the right hand side of the equation
curX = 0
for i in range(len(cMatrix)):
    cMatrix[i].append(eqx.evalf(subs={x:curX}))
    print("curX:",curX)
    curX = curX + xDelta

print()

for i in cMatrix:
    print(i)
    
#Convert to Sympy Matrix
print()
system = sp.Matrix(cMatrix)
result = sp.solve_linear_system_LU(system, ys)
print(result)
