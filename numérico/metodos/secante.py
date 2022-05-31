import numpy as np

def secante(f, x_i, dx, max_ite):
    text=""
    x=x_i
    if eval(f) == 0:
        text=f"{x_i} es raíz la función f(x)"
    else:
        ite = 0
        x_f = x_i + dx
        x=x_i
        entr= f.replace('x','y')
        y=x_f
        while(eval(f)*eval(entr) > 0 and ite < max_ite):
            x_i = x_f
            x_f = x_i + dx
            ite += 1
            
        x=x_i
        y=x_f  
        if eval(f)*eval(entr) == 0:
            tol=0.05
            text=f"{x_i} es raíz la función f(x)"
            text=f"{x_i} es raíz con tolerancia {tol}"
        elif eval(f)*eval(entr) < 0:
            text="Entre "f"{x_i} y "f"{x_f} hay raíz de la función f(x)"
        else:
            text="En "f"{max_ite} no se encontró raíz para la función f(x)"
    return text