import numpy as np

def raices_multiples(f, x_i, f_der, f_der2, tol, max_ite):
    if f(x_i) == 0:
        print(f"{x_i} es raíz la función f(x)")
    else:
        ite = 0
        error = tol + 1
        while(error >= tol and ite < max_ite):
            x_n = x_i - ( f(x_i)*f_der(x_i) ) / ( f_der(x_i)**2 - f_der(x_i)*f_der2(x_i))
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
f_der2 = lambda x : np.exp(-x)
raices_multiples(f, 500, f_der, f_der2, 1e-5, 100)