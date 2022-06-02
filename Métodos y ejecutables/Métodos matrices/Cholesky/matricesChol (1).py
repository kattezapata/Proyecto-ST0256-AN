from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox 
import Cholesky


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def enter_matrix():
  try:
    app.withdraw()
    global matriz 
    matriz = Toplevel()
    global values
    values = []
    global N 
    N = int(text_entry.get())
    for i in range(N):
          list = []
          for j in range(N):
                text = Entry(matriz, width=10)
                text.grid(padx=N, pady=N, row=i, column=j)
                list.append(text)
          values.append(list)
          
    bot_matriz= Button(matriz, text="OK!", command=open_window2)
    bot_matriz.grid(column=N-1, row=N)
    matriz.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter the values correctly")

def open_window2():
  try:
    M = [[float(values[i][j].get()) for j in range(N)] for i in range(N)]
    global M_factored 
    M_factored =  Cholesky.cholesky(np.array(M))
    etiqueta.config(text="Cholesky method done")
    bot_L= Button(matriz, text="See Matrix L", command=open_windowL)
    bot_L.grid(column=N, row=N-1)
    bot_U= Button(matriz, text="See Matrix U", command=open_windowU)
    bot_U.grid(column=N, row=N)

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter values correctly")

def open_windowL():
  try:
    matrizL = Toplevel()
    for i in range(N):
          for j in range(N):
                text = Entry(matrizL, width=10)
                text.grid(padx=N, pady=N, row=i, column=j)
                text.insert(0, '{}'.format(M_factored[0][i][j]))

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter values correctly")

def open_windowU():
  try:
    matrizL = Toplevel()
    for i in range(N):
          for j in range(N):
                text = Entry(matrizL, width=10)
                text.grid(padx=N, pady=N, row=i, column=j)
                text.insert(0, '{}'.format(M_factored[1][i][j]))

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter values correctly")

app = Tk()
app.config(width=900, height=600)
#ventana.geometry('642x498')1
app.title("Cholesky method")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Result")
etiqueta.grid(column=2, row=6, sticky=(W,E))

boton = Label(vp, text="Matrix dimensions")
boton.grid(column=1, row=1)

bot= Button(vp, text="OK!", command=enter_matrix)
bot.grid(column=4, row=1)

text_entry = Entry(vp, width=10)
text_entry.grid(column=2, row=1)

app.mainloop()
