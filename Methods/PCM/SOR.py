import numpy as np

def SOR(x0, A, b, tol, niter, w):
    c = 0
    error = tol + 1
    D = np.diag(np.diag(A)) # Diagonal
    L = -np.tril(A, -1)  # Triangular inferior
    U = -np.triu(A, 1) # Triangular superior 

    iterations = []
    while error > tol and c < niter:
        # Matriz de iteracion 
        T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
        # Vector C
        C = w * np.linalg.inv(D - w * L) @ b
        # Metodo de SOR. calculamos nueva aproximacion
        x1 = T @ x0 + C

        # Norma infinita (Maximo valor absoluto)
        E = np.linalg.norm(x1 - x0, np.inf)
        error = E
        x0 = x1
        c += 1

        iterations.append((x1, E))

    if error < tol:
        n = c
        print(f'Es una aproximación de la solución del sistema con una tolerancia = {tol}')
        return iterations, n
    else:
        n = c
        print(f'Fracasó en {niter} iteraciones')
        return iterations, n
