'''
Created on 12 mar. 2021

@author: Ivi
'''
import tkinter
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import Tk, IntVar, Checkbutton, Button, W

ventana = tkinter.Tk()
ventana.title("Conversor de Divisas")
ventana.geometry("600x600")
ventana.resizable(0,0)
ventana.iconbitmap('ico.ico')

tk.Label(ventana, 
       text="Conversión de divisas Euro, Libra Esterlina, Dólar USA", font='5',
       justify = tk.CENTER).place(x=90,y=20)


    
etiqueta = Label(ventana, text="Cantidad a convertir", font='5').place(x=50,y=170)
cantidad = StringVar()
cantidad = Entry(ventana, fg="red3", width=200, textvariable = cantidad)
cantidad = Entry(ventana)

cantidad.place(x=220, y=175)

v=tkinter.StringVar()

combomoneda = ttk.Combobox(ventana, 
                            values=["Euro", 
                                    "Libra Esterlina",
                                    "Dolar USA"])
combomoneda.grid(column=0, row=1)
combomoneda.place(x=400, y=175)

etiqueta = Label(ventana, text="Conversion", font='5').place(x=250,y=250)


tk.Radiobutton(ventana, text=" Euro a Dólar USA", variable=v,
             value="1").place(x=50, y=300)
tk.Radiobutton(ventana, text="Euro a Libras Esterlinas", variable=v, 
             value="2").place(x=220, y=300)     
tk.Radiobutton(ventana, text="Dólar USA a Euro", variable=v, 
             value="3").place(x=390, y=300)
tk.Radiobutton(ventana, text="Libras Esterlinas a Euro", variable=v, 
             value="4").place(x=50, y=350)
tk.Radiobutton(ventana, text="Dólar USA a Libras", variable=v, 
             value="5").place(x=220, y=350)
tk.Radiobutton(ventana, text="Libras a Dólar USA", variable=v, 
             value="6").place(x=390, y=350)
             
result=StringVar()
result.set("")
etiqueta = Label(ventana, text="Resultado", font='5').place(x=200,y=500)
resultado = Label(ventana, textvariable=result, font='5').place(x=300,y=500)
             
def convertir():
    combo=combomoneda.current()
    cambio=int(v.get())
    res=0.0
    print(cantidad.get().__len__())
    if cantidad.get().__len__()>0:
        original=float(cantidad.get())
        print(cambio, combo, original)
        if cambio==1 and combo==0:
            res=original/0.829187
            divisa="Dolares"
        if cambio==2 and combo==0:
            res=original/1.149954
            divisa="Libras"
        if cambio==3 and combo==2:
            res=original*0.829187
            divisa="Euros"
        if cambio==4 and combo==1:
            res=original*1.149954
            print(res)
            divisa="Euros"
        if cambio==5 and combo==2:
            res=original*0.829187/1.149954
            divisa="Libras"
        if cambio==6 and combo==1:
            res=original/0.829187*1.149954
            divisa="Dolares"
        print(res)
    if res >0.0:
        converti=str(res)
        result.set(converti+" "+divisa)
    else:
        result.set("Comprueba los campos")

boton = Button(ventana, text="Convertir",font='5', command=convertir, height=1, width=10, activebackground="#F50743").place(x=250, y=400)
             
ventana.mainloop()