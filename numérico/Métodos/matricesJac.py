from ast import Yield
from cmath import exp
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox 
import Jacobi

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
          
    bot_matriz= Button(matriz, text="OK!", command=enter_vector)
    bot_matriz.grid(column=N-1, row=N)
    matriz.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter values correctly")

   
def enter_vector():
  try:
    #app.withdraw()
    global vector 
    vector = Toplevel()
    global values1
    values1 = []
    for i in range(N):
          text1 = Entry(vector, width=10)
          text1.grid(padx=N, pady=1, row=i, column=1)
          values1.append(text1)
    bot_vector= Button(vector, text="OK!", command=enter_x0)
    bot_vector.grid(column=1, row=N)
    vector.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter values correctly")

def enter_x0():
  try:
    global M
    M= [[float(values[i][j].get()) for j in range(N)] for i in range(N)]
    #app.withdraw()
    global initial 
    initial = Toplevel()
    global values2
    values2 = []
    for i in range(N):
          text2 = Entry(initial, width=10)
          text2.grid(padx=N, pady=1, row=i, column=1)
          values2.append(text2)
    bot_initial = Button(initial, text="OK!", command=results)
    bot_initial.grid(column=1, row=N)
    initial.mainloop()

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter values correctly")

def results():
  try:
    tol=float(text_entry3.get())
    ite=int(text_entry4.get())
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
    global solution 
    solution = Jacobi.jacobim(np.array(M),np.array(X),np.array(x0),tol,ite)
    
    bot_L= Button(matriz, text="See X Solution", command=open_solution)
    bot_L.grid(column=N, row=N-1)
    
  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter values correctly")
    
def open_solution():
  try:
    sol = Toplevel()
    for i in range(N):
      text = Entry(sol, width=10)
      text.grid(padx=N, pady=N, row=i, column=1)
      text.insert(0, '{}'.format(float(solution[0][i])))
    label_text = "Error: " + solution[1][i]
    label = Label(sol, text=label_text)
    label.grid(column=1, row=N+1, sticky=(W,E))

  except ValueError:
    tkinter.messagebox.showerror(title="Error", message="Please enter values correctly")

app = Tk()
app.config(width=900, height=600)
#ventana.geometry('642x498')1
app.title("Jacobi method")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

v1 = Frame(app)
v1.grid(column=0, row=0, padx=(50,50), pady=(10,10))
v1.columnconfigure(0, weight=1)
v1.rowconfigure(0, weight=1)

label = Label(vp, text="Result")
label.grid(column=2, row=6, sticky=(W,E))

boton = Label(vp, text="Matrix dimension")
boton.grid(column=1, row=1)

bot= Button(vp, text="OK!", command=enter_matrix)
bot.grid(column=4, row=1)


bot= Button(vp, text="OK!", command=enter_vector)
bot.grid(column=5, row=1)

text_entry = Entry(vp, width=10)
text_entry.grid(column=2, row=1)

boton2 = Label(vp, text="Enter tolerance")
boton2.grid(column=1, row=3)

boton3 = Label(vp, text="Maximum number of iterations")
boton3.grid(column=1, row=4)

valor1 = ""
text_entry = Entry(vp, width=10, textvariable=valor1)
text_entry.grid(column=2, row=1)


valor3 = ""
text_entry3 = Entry(vp, width=10, textvariable=valor3)
text_entry3.grid(column=2, row=3)

valor4 = ""
text_entry4 = Entry(vp, width=10, textvariable=valor4)
text_entry4.grid(column=2, row=4)
app.mainloop()