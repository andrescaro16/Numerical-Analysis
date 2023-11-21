from latex2sympy2 import latex2sympy, latex2latex
import pandas as pd
import sympy


import sympy

def bisection(fx: str, a: float, b: float, tol: float, niter: int, et: str) -> tuple:
    x = sympy.symbols('x')
    f = sympy.sympify(fx)
    
    fa = f.subs(x, a)
    fb = f.subs(x, b)
    
    if fa * fb > 0:
        raise ValueError('La función debe cambiar de signo en el intervalo')
    
    if et == 'Decimales Correctos':
        er = sympy.Abs(b-a)
    elif et == 'Cifras Significativas':
        er = sympy.Abs((b-a)/a)
    else:
        raise ValueError('Tipo de error no reconocido')
    
    i = 1
    c = a  # Just an initial value, will be updated in the loop
    
    while er > tol and i <= niter:
        c = (a+b)/2
        fc = f.subs(x, c)
        
        if fc == 0 or sympy.Abs(fc) < tol:
            break
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        if et == 'Decimales Correctos':
            er = sympy.Abs(b-a)
        elif et == 'Cifras Significativas':
            er = sympy.Abs((b-a)/a)
        
        i += 1
    
    return c, i, er