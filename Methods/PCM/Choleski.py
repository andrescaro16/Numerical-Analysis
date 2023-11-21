import numpy as np

def choleski(A):
    n = len(A)
    L = np.zeros((n, n))

    matrix = np.array(A)
    matrixT = np.transpose(matrix)

    if not np.allclose(matrix, matrixT, rtol=1e-8) or not np.all(np.linalg.eigvals(matrix) > 0):
        raise ValueError("La matriz no esta bien definida.")

    
    for i in range(n):
        for j in range(i + 1):
            suma = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j: # elementos de la diagonal
                sqrt_term = A[i][i] - suma
                if sqrt_term < 0:
                    raise ValueError("La matriz no es definida positiva.")
                L[i][j] = np.sqrt(sqrt_term)
            else: # Elementos fuera de la diagonal
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - suma))

    return L