from latex2sympy2 import latex2sympy, latex2latex
import pandas as pd
import sympy


def regla_falsa(fx: str, a: float, b: float, et: bool, tol: float, k:int) -> float:
    """
    Calcula la suma de dos números.

    Args:
        fx: En string que contiene la expresión a evaluar en formato LaTEX.
        a: La cota inferior del intervalo en el que se buscara la raiz.
        b: La cota superior del intervalo en el que se buscara la raiz.
        tol: La tolerancia del error.
    Returns:
        La suma de los dos números.
    """
    tabla = pd.DataFrame(columns=['Valor de a', 'Valor de b', 'Valor de xm', 'Error'])
    sympy_exp = latex2sympy(fx)

    try:
        fn = sympy.sympify(sympy_exp)
        fa = fn.subs({'x': a})
        fb = fn.subs({'x': b})
        fa = fa.evalf()
        fb = fb.evalf()
    except:
        raise ValueError('La funcion no es valida')
    if fa * fb > 0:
        raise ValueError('No hay raiz en el intervalo')
    if fa == 0 or fb == 0:
        raise ValueError('Uno de los extremos es raiz coja seriedad')

    error = tol+1
    xm_1 = 0
    n = 0

    while error > tol and n < k:
        xm = (a * fb - b * fa) / (fb - fa)
        fxm = fn.subs({'x': xm})
        fxm = fxm.evalf()
        if fa * fxm < 0:
            b = xm
            fb = fxm
        else:
            a = xm
            fa = fxm

        if n > 0:
            error = abs(xm - xm_1)
            xm_1 = xm

        tabla = tabla._append({'Valor de a': a, 'Valor de b': b, 'Valor de xm': xm, 'Error': error}, ignore_index=True)
        n += 1
    html = tabla.to_html()

    if n >= k:
        return (html,'El metodo fallo en {} iteraciones'.format(k))
    else:
        return (html,'El metodo convergio a la solución {} con un error menor a {}'.format(xm,tol))