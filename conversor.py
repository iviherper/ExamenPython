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
ventana.iconbitmap('ico.ico')

tk.Label(ventana, 
       text="Conversión de divisas Euro, Libra Esterlina, Dólar USA""", font='5',
       justify = tk.CENTER, padx=90, pady=20).place(x=0,y=0)

ventana.mainloop()