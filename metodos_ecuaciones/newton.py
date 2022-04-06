import numpy as np

def newton(f, x_i, f_der, tol, max_ite):
    if f(x_i) == 0:
        print(f"{x_i} es raíz la función f(x)")
    else:
        ite = 0
        error = tol + 1
        while(error >= tol and ite < max_ite):
            x_n = x_i - f(x_i) / f_der(x_i)
            error = abs(x_n - x_i)
            ite += 1
            x_i = x_n
        if error < tol:
            print(f"{x_i} es raíz con tolerancia {tol}")
        else:
            print("F")
    return

f = lambda x : np.exp(-x) - x
f_der = lambda x : -np.exp(-x) - 1
newton(f, 500, f_der, 1e-5, 100)
