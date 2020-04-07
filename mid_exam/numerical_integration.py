import sympy as sp
from math import pi, sqrt

def simpson_rule(equation, a, b, n):
    """
    Method to get the integration approximation of a function using simpson rule
    
    Parameters:
    equation: The equation f(x)
    a: lower bound of the integral
    b: upper bound of the integral
    n: no of segments
    """
    
    h = abs(b-a)/n
    x = sp.Symbol('x')
    xVal = a
    
    result = 0
    #First segment
    result += equation.evalf(subs={x:xVal})
    #Other segments
    for i in range(1, n):
        if (i == n-1):  #If last segment
            result += equation.evalf(subs={x:xVal})
        else:
            if (i % 2 == 2):
                result += equation.evalf(subs={x:xVal}) * 4
            else:
                result += equation.evalf(subs={x:xVal}) * 2
        xVal += h
    
    result *= h/3
    
    return result

def trapezoid_rule(equation, a, b, n):
    """
    Method to get the integration approximation of a function using trapezoid rule
    
    Parameters:
    equation: The equation f(x)
    a: lower bound of the integral
    b: upper bound of the integral
    n: no of segments
    """
    
    h = abs(b-a)/n
    x = sp.Symbol('x')
    xVal = a
    
    result = 0
    #First segment
    result += equation.evalf(subs={x:xVal})
    #Other segments
    for i in range(1, n):
        if (i == n-1):  #If last segment
            result += equation.evalf(subs={x:xVal})
        else:
            result += equation.evalf(subs={x:xVal}) * 2
        xVal += h
    
    result *= h/2
    
    return result

#Example usage

def gaussian_quadrature_2_points(equation, a, b):
    """
    Method to get the integration approximation of a function using Gaussian Quadrature with two points
    
    Parameters:
    equation: The equation f(x)
    a: lower bound of the integral
    b: upper bound of the integral
    """
    
    x = sp.Symbol('x')

    c1 = (b-a)/2
    c2 = c1
    x1 = c1 * (-1 * (1/sqrt(3))) + (b+a)/2
    x2 = c1 * (1/sqrt(3)) + (b+a)/2
    
    answer = c1 * equation.evalf(subs={x: x1}) + c2 * equation.evalf(subs={x: x2})
    
    return answer

def example():
    x = sp.Symbol('x')
    equa = 8 + 4 * sp.cos(x)
    segments = 4
    a = 0
    b = pi/2
    print(simpson_rule(equa, a, b, segments))
    print(trapezoid_rule(equa, a, b, segments))
    print(gaussian_quadrature_2_points(equa, a, b))