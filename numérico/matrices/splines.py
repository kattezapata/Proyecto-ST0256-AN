#Este programa halla el spline lineal que interpola los datos dados usando el
#metodo de trazadores lineales

#Entradas: 
#X, abscisas 
#Y, ordenadas

#Salidas
#Coef, coeficientes de los trazadores


from operator import length_hint


def Coef():
  C22_trazlin(X,Y)

#Inicializaci�n

def zeros(l):
    for i in range(len(l)):
        l[i]=0;
        
n=length(X);
m=2*(n-1);
A=zeros(m); 
b=zeros(m,1);

Coef=zeros(n-1,2);

#Ciclos
#Condiciones de interpolaci�n
for i in range(n-1):
  i=i+1
  A[i+1,[2*i-1, 2*i]]=[X(i+1), 1]
 # b[i+]=Y[i+1]


#A[1,[1 2]]=[X(1) 1]
b[1]=Y[1];
#Condiciones de continuidad
for i in range(n-2):
    i=i+2
    A[len(X)-1+i,2*i-3:2*i]=[X[i],-X[i]];
    b[len(X)-1+i]=0;  

#Entrega de resultados
Saux=A/b;
#Se organiza la matriz de salida
for i in range(n-1):
    i=i+1
  #  Coef[i]=Saux[2*i-1 2*i]
