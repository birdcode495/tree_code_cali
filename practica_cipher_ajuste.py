import tkinter as tk
from tkinter import ttk
from playsound import playsound
import random
from tkinter import messagebox
import sqlite3
from Base_datos_lista_especies import *
from Pruebas2 import *
from Fotografias_especies import *
from CipherTexts import *



raiz = tk.Tk()
raiz.title("TREE CODE")
raiz.resizable(0,0)
raiz.geometry("795x650")
#notebk = ttk.Notebook(raiz)
marcoPresnte = tk.Frame(raiz)
#notebk.add(marcoPresnt, text = "BioHang")
marcoPresnte.pack()

cipherText_nbk1_jg = cipherText_nbk1

fd = [0, 1]

indic = random.randint(0, len(fd) - 1)


text_cipher_var = tk.StringVar()
text_cipher_var = tk.StringVar(value=cipherText_nbk1_jg[indic])

keyInput = tk.StringVar()


cipher = tk.Label(marcoPresnte, textvariable=text_cipher_var, font=("Arial", 9), justify="center")
cipher.pack()
cipher.config(background="black", fg="#ffffff", width=45, height=20)

key_caesar = tk.Entry(marcoPresnte, textvariable=keyInput, width=7, font=("Arial", 18), justify="center")
key_caesar.config(fg="red", bg="black")
key_caesar.pack()

caesar = tk.Button(marcoPresnte, text = "Decrypt ciphertext", command=lambda:getTranslatedMessage(cipherMode(), getMessage(), getKey_nbk1()))
caesar.config(fg = "green")
caesar.pack()


modeCount = 0


def cipherMode():

	global modeCount
	
	modeCount += 1

	if modeCount % 2 != 0:

		mode = 'd'

	else:
		mode = 'e'

	return mode


def getMessage():

	global message2

	#global text_cipher_var

	message = text_cipher_var.get()

	return message


def getKey_nbk1():

	global keyInput
	
	key = int(keyInput.get())

	return key
	print(key)


def getTranslatedMessage(mode, message, key):

	# #global text_cipher_var

	if mode == 'e':

	 	key = -key

	# translated = ''

	# #message2 = message.get()

	# #text_cipher_var.set(value='')

	

	y = 0

	while y < len(message):

		letr = message[y]
		
		if letr.isalpha():



			num = ord(letr)
			num -= key

			if letr.isupper():

				if num > ord('Z'):
					num -= 26

				elif num < ord('A'):
					num += 26

			elif letr.islower():

				if num > ord('z'):
					num -= 26

				elif num < ord('a'):
					num += 26

			#translated += chr(num)

			text_cipher_var.set(text_cipher_var.get()[:y] + chr(num))
			cipher.config(justify="center")

		else:

			symbol = message[y]

			text_cipher_var.set(text_cipher_var.get()[:y] + symbol)

		y = y + 1




			
		



	 	


		

		

		

		
# mode_nbk1 = cipherMode()
# message_nbk1 = getMessage()
# key_nbk1 = getKey_nbk1()


raiz.mainloop()