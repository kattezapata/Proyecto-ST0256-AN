import numpy as np

def punto_fijo(f, x_i, g, tol, max_ite):
    if f(x_i) == 0:
        print(f"{x_i} es raíz la función f(x)")
    else:
        ite = 0
        error = tol + 1
        while(error >= tol and ite < max_ite):
            x_n = g(x_i)
            error = abs(x_n - x_i)
            ite += 1
            x_i = x_n
        if error < tol:
            print(f"{x_i} es raíz con tolerancia {tol}")
        else:
            print("F")
    return

f = lambda x : np.exp(-x) - x
g = lambda x : np.exp(-x)
punto_fijo(f, 500, g, 1e-5, 100)