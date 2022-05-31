
#import numpy as np
from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk

from metodos import busquedas, biseccion, newton, punto_fijo, raices_multiples, regla_falsa, secante


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np



#raices_multiples(f, x_i, f_der, f_der2, tol, max_ite):
#6. Raices multiples
def raices_multiples_click():
 try:
  _xi = int(entrada_texto.get())
  _f=entrada_texto1.get()
  _f_der=entrada_texto2.get()
  _f_der2=entrada_texto3.get()
  _tol=float(entrada_texto4.get())
  _max=int(entrada_texto5.get())
  #_f= eval(entrada_texto2.get())
  
  #f = lambda x : x
 # f = lambda x : np.sin(x)
 #f = lambda x : np.exp(-x) - x
#f_der = lambda x : -np.exp(-x) - 1
#f_der2 = lambda x : np.exp(-x)
#raices_multiples(f, 500, f_der, f_der2, 1e-5, 100)
  _valor =  raices_multiples.raices_multiples(_f,_xi, _f_der,_f_der2, _tol, _max)
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


m_raices_multiples = Tk()
m_raices_multiples.config(width=900, height=600)
#ventana.geometry('642x498')
m_raices_multiples.title("Método raices multiples")

#Ventana Principal
vp = Frame(m_raices_multiples)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=8, sticky=(W,E))

boton = Label(vp, text="X inicial")
boton.grid(column=1, row=1)

boton1 = Label(vp, text="Función f en términos de x")
boton1.grid(column=1, row=2)

boton2 = Label(vp, text="Función f der en términos de x")
boton2.grid(column=1, row=3)

boton3 = Label(vp, text="Función f der 2 en términos de x")
boton3.grid(column=1, row=4)

boton4 = Label(vp, text="´Tolerancia")
boton4.grid(column=1, row=5)

boton5 = Label(vp, text="´Máximo iterador")
boton5.grid(column=1, row=6)

bot= Button(vp, text="OK!", command=raices_multiples_click)
bot.grid(column=4, row=1)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)

valor1 = ""
entrada_texto1 = Entry(vp, width=10, textvariable=valor1)
entrada_texto1.grid(column=2, row=2)

valor2 = ""
entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
entrada_texto2.grid(column=2, row=3)

valor3 = ""
entrada_texto3 = Entry(vp, width=10, textvariable=valor3)
entrada_texto3.grid(column=2, row=4)

valor4 = ""
entrada_texto4 = Entry(vp, width=10, textvariable=valor4)
entrada_texto4.grid(column=2, row=5)

valor5 = ""
entrada_texto5 = Entry(vp, width=10, textvariable=valor5)
entrada_texto5.grid(column=2, row=6)

m_raices_multiples.mainloop()


