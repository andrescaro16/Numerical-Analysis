import numpy as np

# A = LU
def doolittle_function(A):
    n = len(A)
    L = np.eye(n)  # Inicializa la matriz L como una matriz identidad
    U = np.zeros((n, n))  # Inicializa la matriz U con ceros

    for i in range(n):
        # Calcula la matriz U
        for k in range(i, n):
            suma = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - suma

        # Calcula la matriz L
        for k in range(i, n):
            if i != k:
                suma = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - suma) / U[i][i]

    return (L, U) # Matriz triangular infefrior y Matriz triangular superior