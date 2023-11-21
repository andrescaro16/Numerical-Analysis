import numpy as np

def Jacobi(A, B, X0, tol, iter):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    X0 = np.array(X0, dtype=float)
    dimension = np.shape(A)[0]
    X = np.copy(X0)
    n = 0
    error = tol + 1

    while n < iter and error > tol:
        X_new = np.copy(X)  # Create a copy of X for the new values
        for i in range(dimension):
            suma = 0
            for j in range(dimension):
                if i != j:
                    suma = suma - A[i, j] * X[j]
            X_new[i] = (B[i] + suma) / A[i, i]

        error = np.max(np.abs(np.dot(A, X_new) - B))
        X = X_new  # Update the old X with the new values
        n += 1

    resultado = np.column_stack((np.core.defchararray.add("X", np.arange(1, len(X) + 1).astype(str)), X))

    return resultado, n