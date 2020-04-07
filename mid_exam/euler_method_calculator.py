import sympy as sp

def get_euler_method_table(dydx, x0, y0, n:int, step, x = sp.Symbol('x'), y = sp.Symbol('y')):
    """
    Method to get the values of x, y and dy/dx using euler method in a form of a 2d list
    
    Parameters:
    dydx: Equation to get the derivative
    x0: initial value of x
    y0: initial value of y
    n: number of iterations
    step: value of increment for x
    x: x Symbol object
    y: y Symbol object
    """
    sets = []
    sets.append([x0, y0, dydx.evalf(subs={x: x0, y: y0})])
    for i in range(1, n+1):
        yDelta = sets[i-1][-1] * step
        yNew = sets[i-1][1] + yDelta
        xNew = sets[i-1][0] + step
        sets.append([xNew, yNew, dydx.evalf(subs={x: xNew, y: yNew})])
    
    return sets

def example():
    #Usage example     
    step = 1
    y = sp.Symbol('y')
    diff1 = y
    #y(xInit) = yInit
    xInit = 0
    yInit = 1
    n = 3 #Iterations
    
    sets = get_euler_method_table(diff1, xInit, yInit, n, step)
    for s in sets:
        print(s)