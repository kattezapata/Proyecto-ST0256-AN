import numpy as np

#Este programa halla la solución a la ecuación f(x)=0 en el intervalo [x_i,x_f]
#usando el método de la bisección. 

#Entradas: 
#f, función continua
#x_i, extremo derecho del intervalo inicial
#x_f, extremo final del intervalo final
#tol, tolerancia
#max_ite, número máximo de iteraciones

#Salidas
#x, solución
#iter, número de iteraciones
#err, error

#function [x,iter,err]=C2_biseccion(f,a,b,tol,Nmax)

def Bis(f, x_i, x_f, tol, max_ite):

  #el punto a es (x_i, f(x_i))y el punto b es (x_f, f(x_f))

  #Inicialización
  #m=f(x_f)-f(x_i)/x_f-x_i #pendiente
  #y=m*(x-x_i)/f(x_i)#función
  #fx_i=f(x_i);
  x_m=(x_i+x_f)/2;
  fx_m=f(x_m);
  E=1000; 
  cont=1;
  
  while E>tol and cont < max_ite:
    if f(x_i)*fx_m<0:
       x_f=x_m
    else:
       x_i=x_m;    
    x_0=x_m;
    x_m=(x_i+x_f)/2
    #(f(b)*a-f(a)*b)/(f(b)-f(a));
    fx_m=f(x_m)
    E=abs(x_m-x_0)
    cont=cont+1

  x=x_m
  iter=cont
  err=E
  
  print("X: "f"{x} iter:"f"{iter} err: "f"{err}")

f = lambda x : np.sin(x)

Bis(f, -2, 2, 0.05, 100)