

#import numpy as np
from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
#from matrices import EGsencilla, EGpivoteo_parcial, EGpivoteo_total, Jacobi,interpolacion_newton, Vandermonde, seidel, factorizacionLU, splines, Crout, Doolittle, Cholesky


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def gaussiana_sencilla(M):
    n = len(M)
    M = M.astype('float64')
    for i in range(n):
        for j in range(n-1, i, -1):
            M[j] = M[j] - M[i]*(M[j][i]/M[i][i])
    return M


#1. Eliminación Gaussiana sencilla
def EGsencilla_click():
 try:
  _m = entrada_texto.get()
  #_f= eval(entrada_texto2.get())
  
  #f = lambda x : x
 # f = lambda x : np.sin(x)
  _valor =  EGsencilla.gaussiana_sencilla(_m)
  etiqueta.config(text=_valor)
  

  x = np.arange(1, 100)
  y = x 
  plt.title("Graphic")
  plt.xlabel("x axis caption")
  plt.ylabel("y axis caption")
  plt.plot(x, y)
  plt.show()

 except ValueError:
  etiqueta.config(text="Resultado")


m_EGsencilla = Tk()
m_EGsencilla.config(width=900, height=600)
#ventana.geometry('642x498')
m_EGsencilla.title("Método Eliminación Gaussiana Sencilla")

#Ventana Principal
vp = Frame(m_EGsencilla)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=6, sticky=(W,E))


n = Label(vp, text="Tamaño matriz")
n.grid(column=1, row=1)
matriz=[]
for i in range(n):
    for j in range(n):
        matriz[i][j]= Label(vp, text=("Elemento fila"))
        #elemento= Label(vp, text=("Elemento fila",i," columna",j))
        matriz[i][j].grid(column=j, row=i)
        
        

 #Usa grid!!
def most():
    e=matriz[0]
    root = Tk()
    root.title("matriz A")
    root.config(bg="black")
    for g in range(len(e)):
        for c in range(len(e[g])):
            cell = Entry(root, width=10)
            cell.grid(row=g, column=c)
            cell.insert(0, '{}'.format(e[g][c]))
    root.mainloop()

bot= Button(vp, text="OK!", command=EGsencilla_click)
bot.grid(column=4, row=1)

valor1 = ""
entrada_texto = Entry(vp, width=10, textvariable=valor1)
entrada_texto.grid(column=2, row=1)

#valor2 = ""
#entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
#entrada_texto2.grid(column=2, row=2)




m_EGsencilla.mainloop()
#matrix = np.array([[4,3,-2,-7],[3,12,8,-3],[2,3,-9,3],[1,-2,-5,6]])
#M = gaussiana_sencilla(matrix)
#print(M)