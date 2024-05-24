import tkinter as tk
from playsound import playsound
import random
from tkinter import messagebox
import sqlite3


raiz = tk.Tk()
raiz.title("TREE CODE")
raiz.resizable(0,0)
#raiz.geometry("650x350")
marcoPresnt = tk.Frame(raiz)
marcoPresnt.pack()


nickname = tk.StringVar()

riddle_init = tk.PhotoImage(file="Create_riddle.png")

prim_pantalla = tk.PhotoImage(file="Primera_pantalla5.png")
Presentacion = tk.Label(marcoPresnt, image=prim_pantalla)
Presentacion.pack()

nicknameText = tk.Label(marcoPresnt, text = "Nickname", font = ("Comic Sans MS", 12))
nicknameText.config(fg = "white", bg = "green")
nicknameText.place(x=115, y=20)

nicknameCuad = tk.Entry(marcoPresnt, textvariable=nickname, font = ("Comic Sans MS", 13), justify = "center")
nicknameCuad.config(bg="black", fg="green")
nicknameCuad.place(x=50, y=55)

actBoton = tk.Button(marcoPresnt, text="Activate player", font = ("Comic Sans MS", 13), command=lambda:crearJugador())
actBoton.config(fg="green")
actBoton.place(x=250, y=470)

quitBoton = tk.Button(marcoPresnt, text="Quit game", font = ("Comic Sans MS", 13), command=lambda:quitjuego())
quitBoton.config(fg="green")
quitBoton.place(x=410, y=470)

riddle_init_bt = tk.Button(marcoPresnt, image = riddle_init)
riddle_init_bt.place(x=610, y=445)


raiz.mainloop()