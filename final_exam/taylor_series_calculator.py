import sympy as sp

def calc_taylor_series(equation, xInit, a, n:int):
    """
    Method to estimate a function using taylor series
    
    Parameters:
    equation: The equation f(x)
    xInit: Initial value of x
    a: Another value of x
    n: number of derivatives
    """
    #Variables and settings
    x = sp.Symbol('x')
    fOri = equation
    xVal = xInit  #Initial value of x
    derivatives = []
    
    #Create derivatives
    derivatives.append(fOri)
    for i in range(1, n+1):
        derivatives.append(sp.diff(derivatives[i-1]))
        
    #Calculate derivatives
    for i in range(len(derivatives)):
        derivatives[i] = derivatives[i].evalf(subs={x: a})
        
    #Calculate series
    result = 0
    for i in range(len(derivatives)):
        result += (derivatives[i] * (xVal - a)**i)/sp.factorial(i)
        
    return result

def calc_maclaurin_series(equation, xInit, n:int):
    """
    Method to estimate a function using maclaurin series
    
    Parameters:
    equation: The equation f(x)
    xInit: Initial value of x
    n: number of derivatives
    """
    return calc_taylor_series(equation, xInit, 0, n)

def get_derivatives(equation, n:int):
    derivatives = []
    
    for _ in range(n):
        derivatives.append(sp.diff(equation))
        
    return derivatives

def get_n_derivative(equation, n:int):
    return get_derivatives(equation, n)[-1]

def example():
    x = sp.Symbol('x');
    ori = (sp.sin(x))**3
    print(calc_taylor_series(ori, 0.1, 1.5, 2))