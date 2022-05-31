

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


#4. Punto fijo
def punto_fijo_click():
 try:
  _xi = int(entrada_texto.get())
  _f=entrada_texto1.get()
  _g=entrada_texto2.get()
  _tol=float(entrada_texto3.get())
  _max=int(entrada_texto4.get())
  #_f= eval(entrada_texto2.get())
  
  #f = lambda x : x
 # f = lambda x : np.sin(x)
 #(f, x_i, g, tol, max_ite)
 #
#f = lambda x : np.exp(-x) - x
#g = lambda x : np.exp(-x)
#punto_fijo(f, 500, g, 1e-5, 100)
  _valor =  punto_fijo.punto_fijo(_f,_xi,_g, _tol, _max)
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


m_punto_fijo = Tk()
m_punto_fijo.config(width=900, height=600)
#ventana.geometry('642x498')
m_punto_fijo.title("Método punto fijo")

#Ventana Principal
vp = Frame(m_punto_fijo)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=7, sticky=(W,E))

boton = Label(vp, text="X inicial")
boton.grid(column=1, row=1)

boton1 = Label(vp, text="Función f en términos de x")
boton1.grid(column=1, row=2)

boton2 = Label(vp, text="Función g en términos de x")
boton2.grid(column=1, row=3)

boton3 = Label(vp, text="Tolerancia")
boton3.grid(column=1, row=4)

boton4 = Label(vp, text="´Máximo iterador")
boton4.grid(column=1, row=5)

bot= Button(vp, text="OK!", command=punto_fijo_click)
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


m_punto_fijo.mainloop()
