from latex2sympy2 import latex2sympy, latex2latex
import pandas as pd
import sympy


def biseccion(fx: str, a: float, b: float, tol: float, niter: int) -> tuple:
    tabla = pd.DataFrame(columns=['Iteraciones', 'a', 'c', 'b', 'f(c)', 'Error'])

    try:
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)
        fa = fn.subs({'x': a}).evalf()
        fb = fn.subs({'x': b}).evalf()
    except ValueError as e:
        return None, f'Error: {e}'

    er = abs(b - a)
    i = 1

    while i <= niter and er > tol:
        c = (a + b) / 2
        fc = fn.subs({'x': c}).evalf()

        if fc == 0:
            return tabla.to_html(), f'Solución encontrada en x = {c}'
        if fa * fc < 0:
            b = c
            ct = a
        else:
            a = c
            ct = b
            er = abs(ct - c)

        tabla = tabla._append({'Iteraciones': i, 'a': a, 'c': c, 'b': b, 'f(c)': fc, 'Error': er}, ignore_index=True)
        html = tabla.to_html
        i += 1

    if er < tol:
        return html, f'El método converge en x = {c}'
    elif i > niter:
        return html, f'Solución no encontrada para la tolerancia dada {tol}'
