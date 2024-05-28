import tkinter as tk
from playsound import playsound
import random
from tkinter import messagebox
import sqlite3
from Base_datos_lista_especies import *
import time


conteo = 0

def tree_graphics():

	global conteo

	raiz = tk.Tk()
	raiz.title("TREE CODE")
	raiz.resizable(0,0)
	#raiz.geometry("650x350")
	marcoPresnt = tk.Frame(raiz)
	marcoPresnt.pack()

	x = 0
	crtPlayersonido = "createPlayer.wav"

	pantallas = [[tk.PhotoImage(file="Primera_pantalla5.png"), tk.PhotoImage(file="Acacia_rubinia1.png")], 
	[tk.PhotoImage(file="Mangifera indica2.png")]]
	#prim_pantalla = tk.PhotoImage(file="Primera_pantalla5.png")
	#seg_pantalla = tk.PhotoImage(file="Acacia_rubiniaesc.png")
	Presentacion = tk.Label(marcoPresnt, image=pantallas[0][0])
	Presentacion.pack()

	but = tk.Button(marcoPresnt, text = 'Change', command = lambda:changes())
	but.place(x=10, y=10)



	def changes():

		global conteo

		playsound(crtPlayersonido)
		Presentacion.config(image=pantallas[0][conteo+1])
		but.config(text="Cambia")
		conteo = conteo + 1


		if conteo == len(pantallas[0]) - 1:

			conteo = -1

	raiz.mainloop()


#tree_graphics()