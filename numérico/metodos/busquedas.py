#import numpy as np

def busquedas(f, x_i, dx, max_ite):
    text=""
    if f(x_i) == 0:
        text=f"{x_i} es raíz la función f(x)"
    else:
        ite = 0
        x_f = x_i + dx
        while(f(x_i)*f(x_f) > 0 and ite < max_ite):
            x_i = x_f
            x_f = x_i + dx
            ite += 1
          
        if f(x_i)*f(x_f) == 0:
            text=f"{x_i} es raíz la función f(x)"
            text=f"{x_i} es raíz con tolerancia {tol}"
        elif f(x_i)*f(x_f) < 0:
            text="Entre "f"{x_i} y "f"{x_f} hay raíz de la función f(x)"
        else:
            text="En "f"{max_ite} no se encontró raíz para la función f(x)"
    return text

