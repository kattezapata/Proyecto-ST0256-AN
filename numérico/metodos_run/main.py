

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

#1. Busquedas incrementales
def busquedas_click():
 try:
  _x = int(entrada_texto.get())
  _f=entrada_texto2.get()
  _dx=float(entrada_texto3.get())
  _max=int(entrada_texto4.get())
  #_f= eval(entrada_texto2.get())
  
  #f = lambda x : x
 # f = lambda x : np.sin(x)
  _valor =  busquedas.busquedas(_f,_x, _dx, _max)
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


m_busquedas = Tk()
m_busquedas.config(width=900, height=600)
#ventana.geometry('642x498')
m_busquedas.title("Método busquedas incrementales")

#Ventana Principal
vp = Frame(m_busquedas)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=6, sticky=(W,E))

boton = Label(vp, text="X inicial")
boton.grid(column=1, row=1)

boton2 = Label(vp, text="Función f en términos de x")
boton2.grid(column=1, row=2)

boton3 = Label(vp, text="dx")
boton3.grid(column=1, row=3)

boton4 = Label(vp, text="´Máximo iterador")
boton4.grid(column=1, row=4)

bot= Button(vp, text="OK!", command=busquedas_click)
bot.grid(column=4, row=1)

valor1 = ""
entrada_texto = Entry(vp, width=10, textvariable=valor1)
entrada_texto.grid(column=2, row=1)

valor2 = ""
entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
entrada_texto2.grid(column=2, row=2)

valor3 = ""
entrada_texto3 = Entry(vp, width=10, textvariable=valor3)
entrada_texto3.grid(column=2, row=3)

valor4 = ""
entrada_texto4 = Entry(vp, width=10, textvariable=valor4)
entrada_texto4.grid(column=2, row=4)


#m_busquedas.mainloop()


#2. Biseccion
def biseccion_click():
 try:
  _xi = int(entrada_texto.get())
  _xf = int(entrada_texto1.get())
  _f= entrada_texto2.get()
  _tol=float(entrada_texto3.get())
  _max=int(entrada_texto4.get())
  #_f= eval(entrada_texto2.get())
  
  #f = lambda x : x
 # f = lambda x : np.sin(x)
  #f, x_i, x_f, tol, max_ite
  _valor =  biseccion.biseccion(_f,_xi, _xf, _tol, _max)
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


m_biseccion = Tk()
m_biseccion.config(width=900, height=600)
#ventana.geometry('642x498')
m_biseccion.title("Método biseccion")

#Ventana Principal
vp = Frame(m_biseccion)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=7, sticky=(W,E))

boton = Label(vp, text="X inicial")
boton.grid(column=1, row=1)

boton1 = Label(vp, text="X final")
boton1.grid(column=1, row=2)

boton2 = Label(vp, text="Función f en términos de x")
boton2.grid(column=1, row=3)

boton3 = Label(vp, text="Tolerancia")
boton3.grid(column=1, row=4)

boton4 = Label(vp, text="´Máximo iterador")
boton4.grid(column=1, row=5)

bot= Button(vp, text="OK!", command=biseccion_click)
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


m_biseccion.mainloop()



#3. Newton
def newton_click():
 try:
  _xi = int(entrada_texto.get())
  _f=entrada_texto1.get()
  _f_der=entrada_texto2.get()
  _tol=float(entrada_texto3.get())
  _max=int(entrada_texto4.get())
  #_f= eval(entrada_texto2.get())
  
  #f = lambda x : x
  # f = lambda x : np.sin(x)
  #(f, x_i, f_der, tol, max_ite):
  _valor =  newton.newton(_f,_xi, _f_der, _tol, _max)
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


m_newton = Tk()
m_newton.config(width=900, height=600)
#ventana.geometry('642x498')
m_newton.title("Método Newton")

#Ventana Principal
vp = Frame(m_newton)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=7, sticky=(W,E))

boton = Label(vp, text="X inicial")
boton.grid(column=1, row=1)

boton1 = Label(vp, text="Función f en términos de x")
boton1.grid(column=1, row=2)

boton2 = Label(vp, text="Función f der en términos de x")
boton2.grid(column=1, row=3)

boton3 = Label(vp, text="Tolerancia")
boton3.grid(column=1, row=4)

boton4 = Label(vp, text="´Máximo iterador")
boton4.grid(column=1, row=5)

bot= Button(vp, text="OK!", command=newton_click)
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


#m_newton.mainloop()



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


#m_punto_fijo.mainloop()



#5. Regla falsa
def regla_falsa_click():
 try:
  _xi = int(entrada_texto.get())
  _xf = int(entrada_texto.get())
  _f=entrada_texto2.get()
  _tol=float(entrada_texto3.get())
  _max=int(entrada_texto4.get())
  #_f= eval(entrada_texto2.get())
  
  #f = lambda x : x
 # f = lambda x : np.sin(x)
 #regla_falsa(f, x_i, x_f, tol, max_ite)
  _valor =  regla_falsa.regla_falsa(_f,_xi, _xf, _tol, _max)
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


m_regla_falsa = Tk()
m_regla_falsa.config(width=900, height=600)
#ventana.geometry('642x498')
m_regla_falsa.title("Método regla falsa")

#Ventana Principal
vp = Frame(m_regla_falsa)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=7, sticky=(W,E))

boton = Label(vp, text="X inicial")
boton.grid(column=1, row=1)

boton1= Label(vp, text="X final")
boton1.grid(column=1, row=2)

boton2 = Label(vp, text="Función f en términos de x")
boton2.grid(column=1, row=3)

boton3 = Label(vp, text="Tolerancia")
boton3.grid(column=1, row=4)

boton4 = Label(vp, text="´Máximo iterador")
boton4.grid(column=1, row=5)

bot= Button(vp, text="OK!", command=regla_falsa_click)
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


#m_regla_falsa.mainloop()

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

#m_raices_multiples.mainloop()



#7. Secante
def secante_click():
 try:
  _xi = int(entrada_texto.get())
  _f=entrada_texto2.get()
  _dx=float(entrada_texto3.get())
  _max=int(entrada_texto4.get())
  #_f= eval(entrada_texto2.get())
  
  #f = lambda x : x
  # f = lambda x : np.sin(x)
  #secante(f, x_i, dx, max_ite):
  _valor =  secante.secante(_f,_xi, _dx, _max)
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


m_secante = Tk()
m_secante.config(width=900, height=600)
#ventana.geometry('642x498')
m_secante.title("Método secante")

#Ventana Principal
vp = Frame(m_secante)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=6, sticky=(W,E))

boton = Label(vp, text="X inicial")
boton.grid(column=1, row=1)

boton2 = Label(vp, text="Función f en términos de x")
boton2.grid(column=1, row=2)

boton3 = Label(vp, text="dx")
boton3.grid(column=1, row=3)

boton4 = Label(vp, text="´Máximo iterador")
boton4.grid(column=1, row=4)

bot= Button(vp, text="OK!", command=secante_click)
bot.grid(column=4, row=1)

valor1 = ""
entrada_texto = Entry(vp, width=10, textvariable=valor1)
entrada_texto.grid(column=2, row=1)

valor2 = ""
entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
entrada_texto2.grid(column=2, row=2)

valor3 = ""
entrada_texto3 = Entry(vp, width=10, textvariable=valor3)
entrada_texto3.grid(column=2, row=3)

valor4 = ""
entrada_texto4 = Entry(vp, width=10, textvariable=valor4)
entrada_texto4.grid(column=2, row=4)


#m_secante.mainloop()