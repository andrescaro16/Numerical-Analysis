import numpy as np


def choleski(A):
    n = len(A)
    L = np.zeros((n, n))

    for i in range (n):
        for j in range(i+1):
            suma = sum(L[i][k] * L[j][k] for k in range(j))
            if (i == j):
                L[i][j] = np.sqrt(A[i][i] - suma)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - suma))
    return L
