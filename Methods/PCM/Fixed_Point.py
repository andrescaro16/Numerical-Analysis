from latex2sympy2 import latex2sympy
import pandas as pd
import sympy
import math

def fixed_point(gx: str, x0: float, tol: float, nmax: int, et: str) -> tuple:
    table = pd.DataFrame(columns=['Valor de G(xi)', 'Valor de xi', 'Error'])
    if et != 'Decimales Correctos' and et != 'Cifras Significativas':
        raise ValueError('El tipo de error no es valido')

    try:
        sympy_exp = latex2sympy(gx)
        g = sympy.sympify(sympy_exp)
    except:
        raise ValueError('La función no es valida')

    error = tol + 1
    n = 0
    xant = x0

    while error > tol and n <= nmax:
        try:
            xact = g.subs({'x': xant})
            xact = xact.evalf()

            if math.isnan(xact):
                raise ValueError('La función no es valida')

            if et == 'Decimales Correctos':
                error = abs(xact - xant)
            else:
                error = abs(xact - xant) / abs(xact)
            xant = xact
            table = table._append({'Valor de G(xi)': xact, 'Valor de xi': xant, 'Error': error}, ignore_index=True)
            n += 1
        except:
            raise ValueError('La función no es valida')

    html = table.to_html()
    if n >= nmax:
        return (html, 'El metodo falló en {} iteraciones'.format(nmax))
    else:
        return (html, 'El metodo convergió a la solución {} con un error menor a {}'.format(xant, tol))
