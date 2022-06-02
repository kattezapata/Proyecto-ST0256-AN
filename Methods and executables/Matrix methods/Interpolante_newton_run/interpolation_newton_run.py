from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox 
import interpolation_newton
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


#Newton interpolation Method
def interpolation_newton_click():
  try:
    m_interpolation_newton.withdraw()
    global matriz 
    matriz = Toplevel()
    global N 
    N = int(inputn.get())
    global vector_x
    vector_x = []
    etiquetax = Label(vp, text="X's values")
    etiquetax.grid(column=1, row=0, sticky=(W,E))
    
    for i in range(N):   
        xs = Entry(matriz, width=10)
        xs.grid(padx=N, pady=N, row=i+1, column=1)
          
        vector_x.append(xs)
             
    global vector_y
    vector_y = []
    etiquetay = Label(vp, text="Y's values")
    etiquetay.grid(column=2, row=0, sticky=(W,E))
    
    for i in range(N):   
        ys = Entry(matriz, width=10)
        ys.grid(padx=N, pady=N, row=i+1, column=3)
          
        vector_y.append(ys)
          
    bot_matriz= Button(matriz, text="OK!", command=open_window2)
    bot_matriz.grid(column=N+6, row=N)
    matriz.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Bug", message="Please input rigth values")

def open_window2():
  try:
    vec_x = [float(vector_x[i].get()) for i in range(N)]
    vec_y = [float(vector_y[i].get()) for i in range(N)]
    
    global values 
    values =  interpolation_newton.interpolation_newton(vec_x,vec_y)
    etiqueta.config(text="Newton interpolation done")
    bot_L= Button(matriz, text="See values", command=open_windowL)
    bot_L.grid(column=N+6, row=N+1)
   # bot_U= Button(matriz, text="Ver Matriz U", command=open_windowU)
   # bot_U.grid(column=N, row=N)

  except ValueError:
    tkinter.messagebox.showerror(title="Bug", message="Please input rigth values")

def open_windowL():
  try:
    matrizL = Toplevel()
    for i in range(N):
        texto = Entry(matrizL, width=10)
        texto.grid(padx=N, pady=N, row=i, column=1)
        texto.insert(0, '{}'.format(values[i]))

  except ValueError:
    tkinter.messagebox.showerror(title="Bug", message="Please input rigth values")

def open_windowU():
  try:
    matrizL = Toplevel()
    texto1 = Entry(matrizL, width=10)
    texto1.grid(padx=N, pady=N, row=0, column=1)
    texto1.insert("Resultado")
    
    for i in range(N):
      texto = Entry(matrizL, width=10)
      texto.grid(padx=N, pady=N, row=i+1, column=1)
      texto.insert(0, '{}'.format(values[i]))
        
    

  except ValueError:
    tkinter.messagebox.showerror(title="Bug", message="Please input rigth values")



m_interpolation_newton = Tk()
m_interpolation_newton.config(width=1200, height=800)
m_interpolation_newton.title("Interpolation Newton Method")

#Main window
vp = Frame(m_interpolation_newton)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Result")
etiqueta.grid(column=2, row=6, sticky=(W,E))


n = Label(vp, text="Hoy many points in the form (x,y) you have?")
n.grid(column=1, row=1)

bot= Button(vp, text="OK!", command=interpolation_newton_click)
bot.grid(column=4, row=1)

valor1 = ""
inputn = Entry(vp, width=10, textvariable=valor1)
inputn.grid(column=2, row=1)



m_interpolation_newton.mainloop()
