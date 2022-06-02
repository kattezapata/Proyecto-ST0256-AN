from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox 
import Vandermonde


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def ingresar_datos():
  try:
    app.withdraw()
    global matriz 
    matriz = Toplevel()
    global values
    values = []
    global N 
    N = int(entrada_texto.get())
    tkinter.messagebox.showinfo("Instrucción", "Ingresa en las columnas los valores de X y Y respectivamente")
    for i in range(N):
          lista = []
          for j in range(2):
                texto = Entry(matriz, width=10)
                texto.grid(padx=N, pady=N, row=i, column=j)
                lista.append(texto)
          values.append(lista)
          
    bot_matriz= Button(matriz, text="OK!", command=abrir_ventana2)
    bot_matriz.grid(column=N-1, row=N)
    matriz.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

def abrir_ventana2():
  try:
    M = np.array([[float(values[i][j].get()) for j in range(2)] for i in range(N)])
    global interpol 
    interpol =  Vandermonde.vandermonde(M.T[0], M.T[1])
    etiqueta.config(text="Interpolación realizada")
    bot_L= Button(matriz, text="Ver coeficientes resultantes", command=mostrar_coef)
    bot_L.grid(column=N, row=N-1)

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

def mostrar_coef():
  try:
    matrizL = Toplevel()
    for i in range(N):
          texto = Entry(matrizL, width=10)
          texto.grid(padx=N, pady=N, row=1, column=i)
          texto.insert(0, '{}'.format(interpol[i]))

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

app = Tk()
app.config(width=900, height=600)
#ventana.geometry('642x498')1
app.title("Interpolación de Vandermonde")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=6, sticky=(W,E))

boton = Label(vp, text="Número de observaciones")
boton.grid(column=1, row=1)

bot= Button(vp, text="OK!", command=ingresar_datos)
bot.grid(column=4, row=1)

entrada_texto = Entry(vp, width=10)
entrada_texto.grid(column=2, row=1)

app.mainloop()
