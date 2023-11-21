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


def Jacobi_view(A, B, X0, tol, niter):
    df = pd.DataFrame()

    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    X0 = np.array(X0, dtype=float)
    
    dimension = np.shape(A)[0]
    X = np.copy(X0)

    n = 0
    er = tol + 1

    while n < niter and er > tol:
        Xn = np.copy(X)  
        for i in range(dimension):
            suma = 0
            for j in range(dimension):
                if j != i:
                    suma +=  A[i, j] * X[j]
            Xn[i] = (B[i] - suma) / A[i, i]

        er = np.max(np.abs(np.dot(A, Xn) - B))
        X = Xn  
        n += 1
        df = df._append(pd.Series(X, name=n))

    resultado = np.column_stack((np.core.defchararray.add("X", np.arange(1, len(X) + 1).astype(str)), X))
    df.columns = ['X' + str(i + 1) for i in range(dimension)]
    html = df.to_html()

    return html, resultado, n



