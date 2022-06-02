from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox 
import seidel


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
    tkinter.messagebox.showinfo("Instrucción", "Ingresa la matriz A")
    for i in range(N):
          lista = []
          for j in range(N):
                texto = Entry(matriz, width=10)
                texto.grid(padx=N, pady=N, row=i, column=j)
                lista.append(texto)
          values.append(lista)
          
    bot_matriz= Button(matriz, text="OK!", command=ingresar_vector)
    bot_matriz.grid(column=N-1, row=N)
    matriz.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

   
def ingresar_vector():
  try:
    #app.withdraw()
    global vector 
    vector = Toplevel()
    global values1
    values1 = []
    tkinter.messagebox.showinfo("Instrucción", "Ingresa el vector b")
    for i in range(N):
          texto1 = Entry(vector, width=10)
          texto1.grid(padx=N, pady=1, row=i, column=1)
          values1.append(texto1)
    bot_vector= Button(vector, text="OK!", command=ingresar_x0)
    bot_vector.grid(column=1, row=N)
    vector.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

def ingresar_x0():
  try:
    global M
    M= [[float(values[i][j].get()) for j in range(N)] for i in range(N)]
    #app.withdraw()
    global inicial 
    inicial = Toplevel()
    global values2
    values2 = []
    tkinter.messagebox.showinfo("Instrucción", "Ingresa el vector inicial x0")
    for i in range(N):
          texto2 = Entry(inicial, width=10)
          texto2.grid(padx=N, pady=1, row=i, column=1)
          values2.append(texto2)
    bot_inicial = Button(inicial, text="OK!", command=resultados)
    bot_inicial.grid(column=1, row=N)
    inicial.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

def resultados():
  try:
    tol=float(entrada_texto3.get())
    ite=int(entrada_texto4.get())
    # MATRIZ
    global M
    M = [[float(values[i][j].get()) for j in range(N)] for i in range(N)]
    # VECTOR
    global X
    X = [float(values1[i].get()) for i in range(N)]
    # INICIAL
    x0 = [float(values2[i].get()) for i in range(N)]
    print(M)
    print(X)
    print(x0)
    global solucion 
    solucion = seidel.seidel(np.array(M),np.array(X),x0,tol,ite)
    
    bot_L= Button(matriz, text="Ver X Solución", command=abrir_solucion)
    bot_L.grid(column=N, row=N-1)
    
  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")
    
def abrir_solucion():
  try:
    sol = Toplevel()
    print("AQUI")
    print(solucion)
    print(solucion[0])
    for i in range(N):
      texto = Entry(sol, width=10)
      texto.grid(padx=N, pady=N, row=i, column=1)
      texto.insert(0, '{}'.format(float(solucion[0][i])))
    etiqueta_texto = "Error: " + str(solucion[1][i])
    etiqueta = Label(sol, text=etiqueta_texto)
    etiqueta.grid(column=1, row=N+1, sticky=(W,E))

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Por favor ingresa correctamente los valores")

app = Tk()
app.config(width=900, height=600)
#ventana.geometry('642x498')1
app.title("Método Seidel")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

v1 = Frame(app)
v1.grid(column=0, row=0, padx=(50,50), pady=(10,10))
v1.columnconfigure(0, weight=1)
v1.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=6, sticky=(W,E))

boton = Label(vp, text="Ingresa la dimensión de la matriz")
boton.grid(column=1, row=1)

bot= Button(vp, text="OK!", command=ingresar_matriz)
bot.grid(column=4, row=1)


entrada_texto = Entry(vp, width=10)
entrada_texto.grid(column=2, row=1)


boton2 = Label(vp, text="Ingresa la tolerancia")
boton2.grid(column=1, row=3)

boton3 = Label(vp, text="Ingresa el máximo de iteracciones")
boton3.grid(column=1, row=4)


valor1 = ""
entrada_texto = Entry(vp, width=10, textvariable=valor1)
entrada_texto.grid(column=2, row=1)


valor3 = ""
entrada_texto3 = Entry(vp, width=10, textvariable=valor3)
entrada_texto3.grid(column=2, row=3)

valor4 = ""
entrada_texto4 = Entry(vp, width=10, textvariable=valor4)
entrada_texto4.grid(column=2, row=4)
app.mainloop()