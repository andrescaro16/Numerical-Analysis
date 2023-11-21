import numpy as np

def Jacobi(A, B, X0, tol, iter):


    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    X0 = np.array(X0, dtype=float)
    
    dimension = np.shape(A)[0]
    X = np.copy(X0)
    n = 0
    er = tol + 1

    while n < iter and er > tol:
        Xn = np.copy(X)  # Create a copy of X for the new values
        for i in range(dimension):
            suma = 0
            for j in range(dimension):
                if i != j:
                    suma = suma - A[i, j] * X[j]
            Xn[i] = (B[i] + suma) / A[i, i]

        er = np.max(np.abs(np.dot(A, Xn) - B))
        X = Xn  
        n += 1

    resultado = np.column_stack((np.core.defchararray.add("X", np.arange(1, len(X) + 1).astype(str)), X))

    return resultado, n