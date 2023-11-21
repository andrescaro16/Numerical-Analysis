import numpy as np
import pandas as pd

def diagonal_dominante(A):
    A = np.array(A, dtype=float)
    n = np.shape(A)[0]
    for i in range(n):
        diag = abs(A[i, i])
        off_diag = sum(abs(A[i, j]) for j in range(n) if i != j)
        if diag <= off_diag:
            return False
    return True

def radio_espectral(A):
    eigvalores = np.linalg.eigvals(A)
    radio = np.max(np.abs(eigvalores))
    return radio < 1

def converge(A):
    return np.isinf(A).any() == False and np.isnan(A).any() == False
def Gauss_Seidel(A, B, X0, tol, iter):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    X0 = np.array(X0, dtype=float)
    dimension = np.shape(A)[0]
    # X = np.transpose([X0])
    X = np.copy(X0)
    n = 0
    error = tol + 1
    # Error = np.max(np.abs(np.dot(A,X)-B)) o Error = max(abs(Xi+1 - Xi))
    df = pd.DataFrame()

    while n < iter and error > tol:
        for i in range(dimension):
            suma = 0
            for j in range(dimension):
                if i != j:
                    suma = suma - A[i, j] * X[j]
            X[i] = (B[i] + suma) / A[i, i]

        error = np.max(np.abs(np.dot(A, X) - B))
        n += 1
        df = df._append(pd.Series(X, name=n))

    resultado = np.column_stack((np.core.defchararray.add("X", np.arange(1, len(X) + 1).astype(str)), X))
    df.columns = ['x' + str(i + 1) for i in range(dimension)]
    html = df.to_html()
    return resultado, n, html

    return resultado, n