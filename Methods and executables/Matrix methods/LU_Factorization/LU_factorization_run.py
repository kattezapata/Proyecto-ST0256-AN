from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox 
import LU_factorization


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def ingresar_matriz():
  try:
    app.withdraw()
    global matriz 
    matriz = Toplevel()
    global values
    values = []
    global N 
    N = int(entrada_texto.get())
    tkinter.messagebox.showinfo("Instrucción", "Ingresa la matriz a factorizar")
    for i in range(N):
          lista = []
          for j in range(N):
                texto = Entry(matriz, width=10)
                texto.grid(padx=N, pady=N, row=i+1, column=j)
                lista.append(texto)
          values.append(lista)
          
    bot_matriz= Button(matriz, text="OK!", command=abrir_ventana2)
    bot_matriz.grid(column=N-1, row=N+1)
    matriz.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

def abrir_ventana2():
  try:
    M = [[float(values[i][j].get()) for j in range(N)] for i in range(N)]
    global M_factorizada 
    M_factorizada =  factorizacionLU.lu(np.array(M))
    etiqueta.config(text="Factorización realizada")
    bot_L= Button(matriz, text="Ver Matriz L", command=abrir_ventanaL)
    bot_L.grid(column=N, row=N-1)
    bot_U= Button(matriz, text="Ver Matriz U", command=abrir_ventanaU)
    bot_U.grid(column=N, row=N)

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

def abrir_ventanaL():
  try:
    matrizL = Toplevel()
    for i in range(N):
          for j in range(N):
                texto = Entry(matrizL, width=10)
                texto.grid(padx=N, pady=N, row=i, column=j)
                texto.insert(0, '{}'.format(M_factorizada[0][i][j]))

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

def abrir_ventanaU():
  try:
    matrizL = Toplevel()
    for i in range(N):
          for j in range(N):
                texto = Entry(matrizL, width=10)
                texto.grid(padx=N, pady=N, row=i, column=j)
                texto.insert(0, '{}'.format(M_factorizada[1][i][j]))

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

app = Tk()
app.config(width=900, height=600)
#ventana.geometry('642x498')1
app.title("Método factorización LU")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=6, sticky=(W,E))

boton = Label(vp, text="Dimensiones de la matriz")
boton.grid(column=1, row=1)

bot= Button(vp, text="OK!", command=ingresar_matriz)
bot.grid(column=4, row=1)

entrada_texto = Entry(vp, width=10)
entrada_texto.grid(column=2, row=1)

app.mainloop()
