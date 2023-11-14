import pandas as pd
from latex2sympy2 import latex2sympy
import sympy
import math

def busqueda_incremental(fx: str, a: float, b: float, tol: float, k: int):
    tabla = pd.DataFrame(columns=['Intervalo con raices'])

    try:
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)
        fa = fn.subs({'x': a})
        fb = fn.subs({'x': b})
        fa = fa.evalf()
        fb = fb.evalf()
        if math.isnan(fa) or math.isnan(fb):
            raise ValueError('La función no es válida')
    except:
        raise ValueError('La función no es válida')
    if fa * fb > 0:
        raise ValueError('No hay raíz en el intervalo')
    if fa == 0 or fb == 0:
        raise ValueError('Uno de los extremos es raíz, ¡ten seriedad!')
    
    x1 = a
    x2 = x1 + tol
    iteraciones = 0

    while x2 <= b and iteraciones <= k:
        y1 = fn.subs({'x': x1})
        y2 = fn.subs({'x': x2})

        if (y1 < 0 and y2 >= 0) or (y1 >= 0 and y2 < 0):
            intervalo = [x1, x2]
            nuevo_dataframe = pd.DataFrame({'Intervalo con raices': [f"[{x1}, {x2}]"]})
            tabla = pd.concat([tabla, nuevo_dataframe], ignore_index=True)
        
        x1 = x2
        x2 = x1 + tol
        iteraciones += 1
    html = tabla.to_html()
    
    if iteraciones > k:
        return (html, 'El método falló en {} iteraciones'.format(k))
    else:
        return (html, 'El método convergió a la solución')
