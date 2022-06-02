from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox 
import EGsimple
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#1. Simple gaussian elimination Method
def EGsimple_click():
  try:
    m_EGsimple.withdraw()
    global matriz 
    matriz = Toplevel()
    global values
    values = []
    global N 
    N = int(inputn.get())
    for i in range(N):
          list = []
          for j in range(N):
                text = Entry(matriz, width=10)
                text.grid(padx=N, pady=N, row=i+1, column=j)
                list.append(text)
          values.append(list)
          
    global vector
    vector = []
    etiqueta1 = Label(vp, text="Independent vector")
    etiqueta1.grid(column=N+2, row=1, sticky=(W,E))
    
    for i in range(N):   
        texts = Entry(matriz, width=10)
        texts.grid(padx=N, pady=N, row=i+1, column=N+2)
          
        vector.append(texts)
          
    bot_matriz= Button(matriz, text="OK!", command=open_window2)
    bot_matriz.grid(column=N+6, row=N)
    matriz.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Bug", message="Please input rigth values")

def open_window2():
  try:
    M = [[float(values[i][j].get()) for j in range(N)] for i in range(N)]
    vec = [float(vector[i].get()) for i in range(N)]
    global xvalues 
    xvalues =  EGsimple.EGsimple(M,vec)
    etiqueta.config(text="Simple gaussian elimination done")
    bot_L= Button(matriz, text="See X values", command=open_windowL)
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
        texto.insert(0, '{}'.format(xvalues[i]))

  except ValueError:
    tkinter.messagebox.showerror(title="Bug", message="Please input rigth values")

def open_windowU():
  try:
    matrizL = Toplevel()
    for i in range(N):
        texto = Entry(matrizL, width=10)
        texto.grid(padx=N, pady=N, row=i, column=1)
        texto.insert(0, '{}'.format(xvalues[i]))

  except ValueError:
    tkinter.messagebox.showerror(title="Bug", message="Please input rigth values")



m_EGsimple = Tk()
m_EGsimple.config(width=1200, height=800)
m_EGsimple.title("Simple gaussian elimination Method")

#Main window
vp = Frame(m_EGsimple)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Result")
etiqueta.grid(column=2, row=6, sticky=(W,E))


n = Label(vp, text="Matrix size")
n.grid(column=1, row=1)

bot= Button(vp, text="OK!", command=EGsimple_click)
bot.grid(column=4, row=1)

valor1 = ""
inputn = Entry(vp, width=10, textvariable=valor1)
inputn.grid(column=2, row=1)



m_EGsimple.mainloop()
