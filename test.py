import sympy as sp

x = sp.Symbol('x')

equ = -53 + (x + 4) * 26 + (x + 4) * ( x + 2) * -7 + (x + 4) * (x + 2) * (x + 1)

print(sp.simplify(equ))