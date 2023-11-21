from latex2sympy2 import latex2sympy, latex2latex
import pandas as pd
import sympy


import sympy

def biseccion(fx: str, a: float, b: float, tol: float, niter: int, et: str) -> tuple:
    tabla = pd.DataFrame(columns=['Iteraciones', 'a', 'b', 'f(c)', 'Error'])

    sympy_exp = latex2sympy(fx)
    fn = sympy.sympify(sympy_exp)
    
    fa = fn.subs({'x': a}).evalf()
    fb = fn.subs({'x': b}).evalf()


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
        fc = fn.subs({'x': c}).evalf()
        
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
        tabla = tabla._append({'Iteraciones':i, 'a':a, 'b':b, 'f(c)':fc, 'Error':er}, ignore_index=True)

    
    html = tabla.to_html()
    return html, f'El método convergió a la solución {c}'