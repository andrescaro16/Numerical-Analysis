import numpy as np
import sympy as sym

def lagrange(X, Y):
    
    n = len(X)
    x = sym.Symbol('x')
    polynomial = 0
    divisorL = np.zeros(n, dtype = float)
    
    for i in range(0,n,1):
        numerator = 1
        denominator = 1
        for j in range(0,n,1):
            if (j!=i):
                numerator = numerator*(x-X[j])
                denominator = denominator*(X[i]-X[j])
        Li_term = numerator/denominator

        polynomial = polynomial + Li_term*Y[i]
        divisorL[i] = denominator

    simple_poly = polynomial.expand()

    return simple_poly, divisorL
