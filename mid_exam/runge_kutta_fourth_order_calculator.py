import sympy as sp
    
def get_4th_order_rungekutta(dydx, x0, y0, n:int, h, x = sp.Symbol('x'), y = sp.Symbol('y')):
    """
    Method to get the values of x, y and dy/dx using fourth-order Runge-Kutta method in a form of a 2d list
    
    Parameters:
    dydx: Equation to get the derivative
    x0: initial value of x
    y0: initial value of y
    n: number of iterations
    h: value of increment for x
    x: x Symbol object
    y: y Symbol object
    """
    sets = []
    sets.append([x0, y0, dydx.evalf(subs={x: x0, y: y0})])
    for i in range(1, n+1):
        xOld = sets[i-1][0]
        yOld = sets[i-1][1]
        k1 = dydx.evalf(subs={x:xOld, y:yOld})
        k2 = dydx.evalf(subs={x:xOld + h/2, y:yOld + h*k1/2})
        k3 = dydx.evalf(subs={x:xOld + h/2, y:yOld + h*k2/2})
        k4 = dydx.evalf(subs={x:xOld + h, y:yOld + k3 * h})
        
        yNew = yOld + (1.0/6.0) * (k1 + 2*k2 + 2*k3 + k4) * h
        xNew = xOld + h
        
        sets.append([xNew, yNew, dydx.evalf(subs={x:xNew, y:yNew})])
    
    return sets

def example():
    #Usage example 
    sets = get_4th_order_rungekutta(sp.Symbol('y'), 0, 1, 3, 1)
    
    for s in sets:
        print(s)