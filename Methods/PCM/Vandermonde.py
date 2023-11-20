import numpy as np

def vandermonde(X, Y):
    n = len(X)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = X[i] ** j

    inverse = np.linalg.inv(A)

    coef = []
    for i in range(n):
        total = 0
        for j in range(n):
            total += inverse[i, j] * Y[j]
        coef.append(total)

    polynomial = ""
    for i in range(len(coef)):
        if i == 0:
            polynomial += str(coef[i]) + "+"
        elif i == n - 1:
            polynomial += str(coef[i]) + "x^" + str(i)
        else:
            polynomial += str(coef[i]) + "x^" + str(i) + "+"

    return polynomial
