import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.conf import settings

def create_plot(x,y, x_new, y_new):
    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'bo')
    plt.plot(x_new, y_new)
    img_path = os.path.join(settings.BASE_DIR, 'Methods/static/img/newton_interpolante.png')
    plt.savefig(img_path)
    plt.close()

def is_function(points_x):
    if len(points_x) == len(set(points_x)):
        return True
    else:
        return False

def diferencias_divididas(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef


def newton_poli(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

def print_newton_poly(coefs, x_data):
    n = len(x_data)
    poly_str = ""
    for i in range(n):
        term = f"{coefs[i]:.2f}"
        for j in range(i):
            term += f"*(x - {x_data[j]:.2f})"
        poly_str += term
        if i < n - 1:
            poly_str += " + "
    return poly_str

'''plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)
plt.show()
'''