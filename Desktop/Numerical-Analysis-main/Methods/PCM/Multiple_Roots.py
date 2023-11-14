from latex2sympy2 import latex2sympy, latex2latex
import pandas as pd
import sympy
import math


def multiple_roots(fx: str, xi: float, tol: float, k: int, et: str) -> tuple:
    tabla = pd.DataFrame(columns=['Valor de F(xi)', 'Valor de xi', 'Error'])
    if et != 'Decimales Correctos' and et != 'Cifras Significativas':
        raise ValueError('El tipo de error no es valido')

    try:
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)
        fn_1 = sympy.diff(fn)
        fn_2 = sympy.diff(fn_1)
    except:
        raise ValueError('La funcion no es valida')
    error = tol + 1
    n = 0

    while error > tol and n < k:
        try:
            fxi = fn.subs({'x': xi})
            fxi = fxi.evalf()

            fxi_1 = fn_1.subs({'x': xi})
            fxi_1 = fxi_1.evalf()

            fxi_2 = fn_2.subs({'x': xi})
            fxi_2 = fxi_2.evalf()

            if fxi == 0:
                tabla = tabla._append({'Valor de F(xi)': fxi, 'Valor de xi': xi, 'Error': 0}, ignore_index=True)
                break

            if math.isnan(fxi) or math.isnan(fxi_1) or math.isnan(fxi_2):
                raise ValueError('La funcion no es valida')

            xi_1 = xi - (fxi * fxi_1) / ((fxi_1 ** 2) - (fxi * fxi_2))

            if et == 'Decimales Correctos':
                error = abs(xi_1 - xi)
            else:
                error = abs(xi_1 - xi) / abs(xi_1)
            xi = xi_1
            tabla = tabla._append({'Valor de F(xi)': fxi, 'Valor de xi': xi, 'Error': error}, ignore_index=True)
            n += 1
        except:
            raise ValueError('La funcion no es valida')

    html = tabla.to_html()
    if n >= k:
        return (html, 'El metodo fallo en {} iteraciones'.format(k))
    else:
        return (html, 'El metodo convergio a la solución {} con un error menor a {}'.format(xi_1, tol))


#multiple_roots(r'(x+8)^{3}', 34, 0.5e-10, 100,'Decimales Correctos')
