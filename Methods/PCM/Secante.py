from latex2sympy2 import latex2sympy, latex2latex
import pandas as pd
import sympy
import math

def secante(fx: str, xi: float, x0: float, tol: float, niter: int) -> tuple:
    tabla = pd.DataFrame(columns=['Iteraciones', 'Xi', 'f(xi)', 'Error'])

    try:
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)
        fi = fn.subs({'x': xi}).evalf()
        f0 = fn.subs({'x': x0}).evalf()

    except:
        raise ValueError('La función no es válida')

    er = tol + 1
    n = 2
    tabla = tabla._append({'Iteraciones': 0, 'Xi': x0, 'f(xi)': f0, 'Error': ""}, ignore_index=True)
    tabla = tabla._append({'Iteraciones': 1, 'Xi': xi, 'f(xi)': fi, 'Error': ""}, ignore_index=True)
    
    while n <= niter:
        xm = xi - (fi * (x0 - xi) / (f0 - fi))
        er = abs(xm - x0)
        fxm = fn.subs({'x': xm}).evalf()

        tabla = tabla._append({'Iteraciones': n, 'Xi': xm, 'f(xi)': fxm, 'Error': er}, ignore_index=True)
        html = tabla.to_html()
        x0 = xi
        xi = xm
        n += 1

        if er < tol:
            return html, f'El método convergió a la solución {xm} con un error menor a {tol}'
    
    if n > niter:
        return html, f'El método falló en {niter} iteraciones'