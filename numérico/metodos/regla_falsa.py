import numpy as np

def regla_falsa(f, x_i, x_f, tol, max_ite):
 
#
#%Salidas
#%x, solución
#%iter, número de iteraciones
#%err, error

#function [x,iter,err]=C3_reglafalsa(f,a,b,tol,Nmax)
  
  #el punto a es (xi, f(xi))y el punto b es (xf, f(xf))
  #%Inicialización
  m=f(x_f)-f(x_i)/x_f-x_i #pendiente
  #y=m*(x-x_i)/f(x_i)#función
  pm=(f(x_f)*x_i-f(x_i)*x_f)/(f(x_f)-f(x_i))
  fpm=f(pm)
  E=1000
  cont=1
  
  while E>tol and cont < max_ite:
    if f(x_i)*fpm<0:
       x_f=pm
    else:
       x_i=pm;    
    p0=pm;
    x=x_f
    f_xf=eval(f)
    x=x_i
    f_xi=eval(f)
    pm=(f_xf*x_i-f_xi*x_f)/(f_xf-f_xi)
    #(f(b)*a-f(a)*b)/(f(b)-f(a));
    x=pm
    fpm=eval(f)
    E=abs(pm-p0)
    cont=cont+1

  x=pm
  iter=cont
  err=E
  
  text=("X: "f"{x} iter:"f"{iter} err: "f"{err}")
  
  return text
        

