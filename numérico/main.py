
#import numpy as np
import sys
import tkinter as tk
from tkinter import *
from metodos import busquedas


def hacer_click():
 try:
  _valor = int(entrada_texto.get())
  f = lambda x : x
 # f = lambda x : np.sin(x)
  _valor =  busquedas.busquedas(f,_valor, 0.01, 100)
  etiqueta.config(text=_valor)
 except ValueError:
  etiqueta.config(text="Resultado")


app = Tk()
app.config(width=600, height=300)
app.title("Método busquedas incrementales")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Resultado")
etiqueta.grid(column=2, row=2, sticky=(W,E))

boton = Label(vp, text="X inicial")
boton.grid(column=1, row=1)

bot= Button(vp, text="OK!", command=hacer_click)
bot.grid(column=3, row=1)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)



app.mainloop()