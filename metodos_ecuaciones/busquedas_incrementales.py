import numpy as np

def busquedas(f, x_i, dx, max_ite):
    if f(x_i) == 0:
        print(f"{x_i} es raíz la función f(x)")
    else:
        ite = 0
        x_f = x_i + dx
        while(f(x_i)*f(x_f) > 0 and ite < max_ite):
            x_i = x_f
            x_f = x_i + dx
            ite += 1
          
        if f(x_i)*f(x_f) == 0:
            print(f"{x_i} es raíz la función f(x)")
            print(f"{x_i} es raíz con tolerancia {tol}")
        elif f(x_i)*f(x_f) < 0:
            print("Entre "f"{x_i} y "f"{x_f} hay raíz de la función f(x)")
        else:
            print("En "f"{max_ite} no se encontró raíz para la función f(x)")
    return

f = lambda x : np.sin(x)

busquedas(f, 0, 0.01, 100)
