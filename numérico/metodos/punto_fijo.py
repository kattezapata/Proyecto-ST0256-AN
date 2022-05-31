import numpy as np

def punto_fijo(f, x_i, g, tol, max_ite):
    text=""
    x=x_i
    y=eval(f) 
    if y==0:
        text=(f"{x_i} es raíz la función f(x)")
    else:
        ite = 0
        error = tol + 1
        while(error >= tol and ite < max_ite):
            x=x_i
            x_n = eval(g)
            error = abs(x_n - x_i)
            ite += 1
            x_i = x_n
        if error < tol:
            text=(f"{x_i} es raíz con tolerancia {tol}")
        else:
            text=("F, no se encontró raiz")
    return text
