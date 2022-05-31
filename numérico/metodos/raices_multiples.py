import numpy as np

def raices_multiples(f, x_i, f_der, f_der2, tol, max_ite):
    text=""
    x=x_i
    if eval(f) == 0:
        text=(f"{x_i} es raíz la función f(x)")
    else:
        ite = 0
        error = tol + 1
        while(error >= tol and ite < max_ite):
            x=x_i
            f_xi=eval(f)
            f_der_xi=eval(f_der)
            f_der2_xi=eval(f_der2)
            x_n = x_i - ( f_xi*f_der_xi) / ( f_der_xi**2 - f_der_xi*f_der2_xi)
            error = abs(x_n - x_i)
            ite += 1
            x_i = x_n
        if error < tol:
            text=(f"{x_i} es raíz con tolerancia {tol}")
        else:
            text="F, no se encontró raiz"
    return text

