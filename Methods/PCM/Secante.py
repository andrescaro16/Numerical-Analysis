from latex2sympy2 import latex2sympy
import pandas as pd
import sympy
import math

def secante(fx: str, xi: float, x0: float, tol: float, niter: int,et: str) -> tuple:
    tabla = pd.DataFrame(columns=['Iteraciones', 'Xi', 'f(xi)', 'Error'])

    try:
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)
        fi = fn.subs({'x': xi}).evalf()
        f0 = fn.subs({'x': x0}).evalf()

    except Exception as e:
        raise ValueError(f'La función no es válida: {e}')

    tabla = tabla._append({'Iteraciones': 0, 'Xi': x0, 'f(xi)': f0, 'Error': ""}, ignore_index=True)
    tabla = tabla._append({'Iteraciones': 1, 'Xi': xi, 'f(xi)': fi, 'Error': ""}, ignore_index=True)

    n = 2
    er = tol + 1


    while n <= niter and er > tol:
        xm = xi - (fi * (x0 - xi) / (f0 - fi))
        fxm = fn.subs({'x': xm}).evalf()
        
        
        

        if et == 'Decimales Correctos':
            er = sympy.Abs(xm-xi)
        elif et == 'Cifras Significativas':
            er = sympy.Abs((xm - xi/xi))
        else:
            raise ValueError('Error en error')


        tabla = tabla._append({'Iteraciones': n, 'Xi': xm, 'f(xi)': fxm, 'Error': er}, ignore_index=True)
        x0 = xi
        xi = xm
        fi = fxm
        n += 1

    html = tabla.to_html()
    if er < tol:
        return html, f'El método convergió a la solución {xm}'
    else:
        return html, f'El método falló en {niter} iteraciones'
