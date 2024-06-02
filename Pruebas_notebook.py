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
import time


raiz = tk.Tk()
raiz.title("TREE CODE")
raiz.resizable(0,0)
#raiz.geometry("650x350")
#notebk = ttk.Notebook(raiz)
marcoPresnt = tk.Frame(raiz)
#notebk.add(marcoPresnt, text = "BioHang")
marcoPresnt.pack()



graphic = tk.PhotoImage(file="Graphics-logo2.png")
iniRiddle = "inicioRiddle.wav"
crtPlayersonido = "createPlayer.wav"
crtedPlayerExito = "playerActivated.wav"
playerHasNoGems = "noGemsPlayer.wav"
premGem = "premioGem.wav"
explanCoin = "explnCoins.wav"
explanGem = "explnGems.wav"
gemsGanadas = 0
kali = tk.PhotoImage(file="Kali 888-logo4.png")
caesar_img = tk.PhotoImage(file="Caesar_cipher.png")

spanish_name_jg = spanish_name
english_name_jg = english_name
scientific_name_jg = scientific_name
tree_photos_jg = tree_photos
keys_nbk1_jg = keys_nbk1

cipherText_nbk1_jg = cipherText_nbk1

fd = [0, 1]

indic = random.randint(0, len(fd) - 1)

nickname = tk.StringVar()
keyInput = tk.StringVar()
text_cipher_var = tk.StringVar(value=cipherText_nbk1_jg[12])



score = 0
scoreAcumulado = 0
lifes = -1
lifesAc = 0
goldCoins = 0


riddle_init = tk.PhotoImage(file="Create_riddle.png")
english_logo = tk.PhotoImage(file="English-logo2.png")
spanish_logo = tk.PhotoImage(file="Español-logo3.png")
scientific_logo = tk.PhotoImage(file="Scientific-logo2.png")

prim_pantalla = tk.PhotoImage(file="Primera_pantalla5.png")
Presentacion = tk.Label(marcoPresnt, image=prim_pantalla)
Presentacion.pack()

nicknameText = tk.Label(marcoPresnt, text = "Player nickname", font = ("Comic Sans MS", 12))
nicknameText.config(fg = "white", bg = "green")
nicknameText.place(x=95, y=20)

nicknameCuad = tk.Entry(marcoPresnt, textvariable=nickname, font = ("Comic Sans MS", 13), justify = "center")
nicknameCuad.config(bg="black", fg="green")
nicknameCuad.place(x=50, y=55)

actBoton = tk.Button(marcoPresnt, text="Activate player", font = ("Comic Sans MS", 13), command=lambda:crearJugador())
actBoton.config(fg="green")
actBoton.place(x=250, y=470)

quitBoton = tk.Button(marcoPresnt, text="Quit game", font = ("Comic Sans MS", 13), command=lambda:quitjuego())
quitBoton.config(fg="green")
quitBoton.place(x=410, y=470)

riddle_init_bt = tk.Button(marcoPresnt, image = riddle_init, command=lambda:[resetCrLetters(), createNewWindow()])
riddle_init_bt.place(x=610, y=445)

idiom_choose_en = tk.Button(marcoPresnt, image=english_logo, command = lambda:activeEnglish())
idiom_choose_en.config(bg="#ffffff")
idiom_choose_en.place(x=300, y=10)

idiom_choose_es = tk.Button(marcoPresnt, image=spanish_logo, command = lambda:activeSpanish())
idiom_choose_es.config(bg="#ffffff")
idiom_choose_es.place(x=380, y=10)

idiom_choose_sci = tk.Button(marcoPresnt, image=scientific_logo, command = lambda:activeScientific())
idiom_choose_sci.config(bg="#ffffff")
idiom_choose_sci.place(x=460, y=10)

language = ""


def activeEnglish():

	global language

	language = "English"


def activeSpanish():

	global language

	language = "Spanish"


def activeScientific():

	global language

	language = "Scientific"



playsound(iniRiddle)


def quitjuego():

	if nickname.get() != "" and lifes >= 0:

		conexion2 = sqlite3.connect("players")
		cursor2 = conexion2.cursor()

		sql4 = "update playeridiom set (gems, goldcoins, score, gemsgand) = (?, ?, ?, ?) where nickname = (?)"
		datsActs = (lifesAc.get(), goldCoins, score.get(), gemsGanadas, nickname.get())

		cursor2.execute(sql4, datsActs)
		conexion2.commit()
		conexion2.close()

		raiz.destroy()

	elif lifes < 0:
		raiz.destroy()



def crearJugador():

	global record
	global score
	global scoreAcumulado
	global lifes
	global lifesAc
	global goldCoins
	global gemsGanadas

	conexion1 = sqlite3.connect("players")
	cursor1 = conexion1.cursor()

	sql = "insert into playeridiom(nickname, gems, goldcoins, score, gemsgand) values(?, ?, ?, ?, ?)"
	datos = (nickname.get(), 4, 0, 100, 0)
	sql2 = "select * from playeridiom where nickname = (?)"
	dato = (nickname.get(),)

	cursor1.execute(sql2, dato)
	dt = cursor1.fetchall()

	if len(dt) == 0:

		cursor1.execute(sql, datos)
		cursor1.execute(sql2, dato)
		record = cursor1.fetchall()
		score = record[0][4]
		scoreAcumulado = record[0][4]
		lifes = record[0][2] - 1
		lifesAc = record[0][2]
		goldCoins = record[0][3]
		gemsGanadas = record[0][5]
		playsound(crtPlayersonido)
		playsound(crtedPlayerExito)



	elif dt[0][2] > 0:

		score = dt[0][4]
		scoreAcumulado = dt[0][4]
		lifes = dt[0][2] - 1
		lifesAc = dt[0][2]
		goldCoins = dt[0][3]
		gemsGanadas = dt[0][5]
		playsound(crtPlayersonido)
		playsound(crtedPlayerExito)

	elif dt[0][2] <= 0:

		playsound(playerHasNoGems)


	conexion1.commit()
	conexion1.close()


mision = -1
listMision = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14", "M15", "M16",
"M17", "M18", "M19", "M20", "M21", "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M29", "M30", "M31", "M32", "M33",
"M34", "M35", "M36", "M37", "M38", "M39", "M40", "M41", "M42", "M43", "M44", "M45", "M46", "M47", "M48", "M49", "M50",
"M51", "M52", "M53", "M54", "M55", "M56", "M57", "M58", "M59", "M60", "M61", "M62", "M63", "M64", "M65", "M66", "M67",
"M68", "M69", "M70", "M71", "M72", "M73", "M74", "M75", "M76", "M77", "M78", "M79", "M80", "M81", "M82", "M83", "M84",
"M85", "M86", "M87", "M88", "M89", "M90", "M91", "M92", "M93", "M94", "M95", "M96", "M97", "M98", "M99", "M100", "M101",
"M102", "M103", "M104", "M105", "M106", "M107", "M108", "M109", "M110", "M111", "M112", "M113", "M114", "M115", "M116",
"M117", "M118", "M119", "M120", "M121", "M122", "M123", "M124", "M125", "M126", "M127", "M128", "M129", "M130", "M131",
"M132", "M133", "M134", "M135", "M136", "M137", "M138", "M139", "M140", "M141", "M142", "M143", "M144", "M145", "M146",
"M147", "M148", "M149", "M150", "M151", "M152", "M153", "M154", "M155", "M156"]



indice = ""
secretWord = ""
blanks = ""
correctLetters = 0
correctLettersDsp = ""
missedLetters = ""
alreadyLetters = ""
#score = record[4]
#scoreAcumulado = record[4]
wrongs = 0
#lifes = record[2] - 1
#lifesAc = record[2]
gameOver = False
guessSecWord = False
passedMissions = -1
avisoGuess = 0
runOut = False
avisoRunOut = 0
#goldCoins = record[3]
ganancia = "donkey.wav"
perdida = "faily.wav"
ganarPantalla = "monedas_1.mp3"
Verd = tk.PhotoImage(file="Verdugo200.png")
Verd2 = tk.PhotoImage(file="VerdugoPass1.png")
jimmy_es = "jim-fin-es.wav"
jimmy_en = "jim-final-en.wav"
imnUse = tk.PhotoImage(file="IdiomUse.png")
coinbatt = tk.PhotoImage(file="Coin.png")
gembatt = tk.PhotoImage(file="Diamond Tree-logo4.png")
exceUse = "exceptEx.mp3"
risaJim = "Risa_Jimmy.wav"
gemLostt = "Lost_tree.wav"
frag = "frag2.wav"


def cambiarImagen():

	Presentacion.config(image=acth)



def createNewWindow():

	global words
	global idiomMeans
	global listMision
	global mision
	global secretWord
	global indice
	global blanks
	global correctLettersDsp
	global missedLetters
	global score
	global scoreAcumulado
	global guessSecWord
	global passedMissions
	global idiomMeans
	global Verd
	global graphic
	global jimmy
	global imnUse
	global coinbatt
	global gembatt
	global goldCoins
	global lifes
	global lifesAc
	global iniRiddle
	global Verd2
	global marcoAhorc
	global cipherText_nbk1_jg
	global keyInput
	global mode
	global message_nbk1
	global key_nbk1
	global text_cipher_var
		

	if passedMissions == mision and nickname.get() != "" and lifes >= 0 and language != "":

		mision = mision + 1
		
		
		#if mision <= 7:
		#	indice = random.randint(0, 7-mision)

		#elif 7 < mision <= 15:
		#	indice = random.randint(0, 15-mision)

		#elif 15 < mision <= 20:
		#	indice = random.randint(0, 20-mision)

		playsound(iniRiddle)
		indice = random.randint(0, len(spanish_name_jg)-1)

		
		if language == "Spanish":

			secretWord = spanish_name_jg[indice]

		elif language == "English":

			secretWord = english_name_jg[indice]

		elif language == "Scientific":

			secretWord = scientific_name_jg[indice]



		blanks = tk.StringVar(value="*" * len(secretWord))
		correctLettersDsp = tk.StringVar(value="")
		missedLetters = tk.StringVar(value="")
		score = tk.IntVar(value=(0 + scoreAcumulado))
		lifesAc = tk.IntVar(value=lifes + 1)


		listMision[mision] = tk.Toplevel(raiz)
		listMision[mision].geometry("995x600")
		listMision[mision].title("TREE CODE")
		listMision[mision].resizable(0,0)
		listMision[mision].config(bg="#02290A")
				
		notebk = ttk.Notebook(listMision[mision])
		notebk.pack(expand=True)
		
		fr = ttk.Frame(notebk, width = 995, height=600)
		fr.configure(style = "BW.TLabel")
		fr.pack(fill='both', expand=True)
		notebk.add(fr, text = "   Bio Hangman Cali")

		fr2 = ttk.Frame(notebk, width = 995, height=600)
		fr2.pack(fill='both', expand=True)
		notebk.add(fr2, text = "   Urban Criptography")

		style = ttk.Style()
		style.configure("BW.TLabel", background="#02290A", foreground="white")

		s1 = ttk.Style()
		s1.configure("Jimmy.TButton", background="#02290A", foreground="#ffffff")

		text_cipher_var = tk.StringVar(value=cipherText_nbk1_jg[12])

		# l1 = ttk.Label(text="Test", style="BW.TLabel")
		# l2 = ttk.Label(text="Test", style="BW.TLabel")

		#munecoAhorc = tk.PhotoImage(file83ahorcado2.png")
		marcoAhorc = tk.Button(fr, image=Verd, command=lambda:jim())
		marcoAhorc.config(background="#02290A")
		marcoAhorc.place(x=90, y=370)

		

		Bienvenida = ttk.Label(fr, text="TREE CODE", font=("Comic Sans MS", 27), style = "BW.TLabel")
		#Bienvenida.configure(fg="#ffffff", bg="#02290A", padx=10)
		Bienvenida.place(x=80, y=50)

		miFrame = tk.Frame(fr)
		miFrame.place(x=60, y=120)
		#miFrame.config(padx=10, pady=20)

		cipher = tk.Label(fr, textvariable=text_cipher_var, font=("Arial", 8), padx=4)
		cipher.place(x=680, y=392)
		cipher.config(background="black", fg="#ffffff", width=39, height=11, padx=6)

		caesar = tk.Button(fr, text = "Decrypt ciphertext", command=lambda:getTranslatedMessage(cipherMode(), getMessage(), getKey_nbk1()))
		caesar.config(fg = "green")
		caesar.place(x=547, y=420)

		caesar = tk.Button(fr, text = "Caesar cipher", command=lambda:caesar_audio())
		caesar.config(fg = "green")
		caesar.place(x=558, y=530)

		caesar_image = tk.Label(fr, image = caesar_img)
		caesar_image.place(x=545, y=460)

		key_label = tk.Label(fr, text = "Enter Key", font=("Comic Sans MS", 12))
		key_label.place(x=560, y=350)
		key_label.config(fg="#ffffff", bg="#02290A")

		key_caesar = tk.Entry(fr, textvariable=keyInput, width=7, font=("Arial", 18), justify="center")
		key_caesar.config(fg="red", bg="black")
		key_caesar.place(x=552, y=380)

		text_type = tk.Label(fr, text = "Cipher text", font=("Lucida Calligraphy", 20))
		text_type.place(x=720, y=345)
		text_type.config(fg="#ffffff", bg="#02290A")


		#------------------------fila 1-------------------------------------

		botonQ = tk.Button(miFrame, text="A", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("a"), guessSecretWord(), runOutGuess()])
		botonQ.grid(row=0, column=1)
		botonQ.config(fg="green")
		botonW = tk.Button(miFrame, text="B", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("b"), guessSecretWord(), runOutGuess()])
		botonW.grid(row=0, column=2)
		botonW.config(fg="green")
		botonE = tk.Button(miFrame, text="C", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("c"), guessSecretWord(), runOutGuess()])
		botonE.grid(row=0, column=3)
		botonE.config(fg="green")
		botonR = tk.Button(miFrame, text="D", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("d"), guessSecretWord(), runOutGuess()])
		botonR.grid(row=0, column=4)
		botonR.config(fg="green")
		botonT = tk.Button(miFrame, text="E", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("e"), guessSecretWord(), runOutGuess()])
		botonT.grid(row=0, column=5)
		botonT.config(fg="green")

		#------------------------fila 2-------------------------------------

		botonY = tk.Button(miFrame, text="F", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("f"), guessSecretWord(), runOutGuess()])
		botonY.grid(row=1, column=1)
		botonY.config(fg="green")
		botonU = tk.Button(miFrame, text="G", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("g"), guessSecretWord(), runOutGuess()])
		botonU.grid(row=1, column=2)
		botonU.config(fg="green")
		botonI = tk.Button(miFrame, text="H", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("h"), guessSecretWord(), runOutGuess()])
		botonI.grid(row=1, column=3)
		botonI.config(fg="green")
		botonO = tk.Button(miFrame, text="I", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("i"), guessSecretWord(), runOutGuess()])
		botonO.grid(row=1, column=4)
		botonO.config(fg="green")
		botonP = tk.Button(miFrame, text="J", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("j"), guessSecretWord(), runOutGuess()])
		botonP.grid(row=1, column=5)
		botonP.config(fg="green")

		#------------------------fila 3-------------------------------------

		botonA = tk.Button(miFrame, text="K", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("k"), guessSecretWord(), runOutGuess()])
		botonA.grid(row=2, column=1)
		botonA.config(fg="green")
		botonS = tk.Button(miFrame, text="L", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("l"), guessSecretWord(), runOutGuess()])
		botonS.grid(row=2, column=2)
		botonS.config(fg="green")
		botonD = tk.Button(miFrame, text="M", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("m"), guessSecretWord(), runOutGuess()])
		botonD.grid(row=2, column=3)
		botonD.config(fg="green")
		botonF = tk.Button(miFrame, text="N", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("n"), guessSecretWord(), runOutGuess()])
		botonF.grid(row=2, column=4)
		botonF.config(fg="green")
		botonG = tk.Button(miFrame, text="O", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("o"), guessSecretWord(), runOutGuess()])
		botonG.grid(row=2, column=5)
		botonG.config(fg="green")

		#------------------------fila 4-------------------------------------

		botonH = tk.Button(miFrame, text="P", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("p"), guessSecretWord(), runOutGuess()])
		botonH.grid(row=3, column=1)
		botonH.config(fg="green")
		botonJ = tk.Button(miFrame, text="Q", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("q"), guessSecretWord(), runOutGuess()])
		botonJ.grid(row=3, column=2)
		botonJ.config(fg="green")
		botonK = tk.Button(miFrame, text="R", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("r"), guessSecretWord(), runOutGuess()])
		botonK.grid(row=3, column=3)
		botonK.config(fg="green")
		botonL = tk.Button(miFrame, text="S", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("s"), guessSecretWord(), runOutGuess()])
		botonL.grid(row=3, column=4)
		botonL.config(fg="green")
		botonZ = tk.Button(miFrame, text="T", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("t"), guessSecretWord(), runOutGuess()])
		botonZ.grid(row=3, column=5)
		botonZ.config(fg="green")


		#------------------------fila 5-------------------------------------

		botonX = tk.Button(miFrame, text="U", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("u"), guessSecretWord(), runOutGuess()])
		botonX.grid(row=4, column=1)
		botonX.config(fg="green")
		botonC = tk.Button(miFrame, text="V", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("v"), guessSecretWord(), runOutGuess()])
		botonC.grid(row=4, column=2)
		botonC.config(fg="green")
		botonV = tk.Button(miFrame, text="W", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("w"), guessSecretWord(), runOutGuess()])
		botonV.grid(row=4, column=3)
		botonV.config(fg="green")
		botonB = tk.Button(miFrame, text="X", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("x"), guessSecretWord(), runOutGuess()])
		botonB.grid(row=4, column=4)
		botonB.config(fg="green")
		botonN = tk.Button(miFrame, text="Y", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("y"), guessSecretWord(), runOutGuess()])
		botonN.grid(row=4, column=5)
		botonN.config(fg="green")

		#-------------------------fila 6----------------------------------------------

		botonM = tk.Button(miFrame, text="Z", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("z"), guessSecretWord(), runOutGuess()])
		botonM.grid(row=5, column=1)
		botonM.config(fg="green")
		botonApost = tk.Button(miFrame, text="'", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("'"), guessSecretWord(), runOutGuess()])
		botonApost.grid(row=5, column=2)
		botonApost.config(fg="green")
		botonRaya = tk.Button(miFrame, text="-", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("-"), guessSecretWord(), runOutGuess()])
		botonRaya.grid(row=5, column=3)
		botonRaya.config(fg="green")
		botonComa = tk.Button(miFrame, text=",", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada(","), guessSecretWord(), runOutGuess()])
		botonComa.grid(row=5, column=4)
		botonComa.config(fg="green")
		botonPreg = tk.Button(miFrame, text="Ñ", font=("Comic Sans MS", 10), width=4, command=lambda:[letraPulsada("ñ"), guessSecretWord(), runOutGuess()])
		botonPreg.grid(row=5, column=5)
		botonPreg.config(fg="green")
		botonEspacio = tk.Button(miFrame, text="                                                  ", font=("Comic Sans MS", 10), command=lambda:[letraPulsada(" "), guessSecretWord(), runOutGuess()])
		botonEspacio.grid(row=6, column=1, columnspan=5)


		#Rid = tk.Frame(listMision[mision])
		#Rid.grid(row=0, column=1, padx=100)
		#Rid.config(background="#F9D8F8")
		#secretWord = Label(board, text=words[index])
		#secretWord.grid(row=0, column=0)

		#board = tk.Frame(listMision[mision])
		#board.place(x=280, y=10)

		#etiqRiddle = tk.Label(listMision[mision], text="Riddle", font=("Lucida Calligraphy", 13,))
		#etiqRiddle.place(x=440, y=15)
		#etiqRiddle.config(fg="#3A0338", bg="#944DBD")

		#riddle = tk.Label(listMision[mision], text=riddles[indice], font=("Lucida Calligraphy", 12))
		#riddle.place(x=350, y=50)
		#riddle.config(fg="#3A0338", bg="#944DBD")

		etiqSecretWord = tk.Label(fr, text="Tree's Secret name", font=("Comic Sans MS", 20))
		etiqSecretWord.place(x=530, y=20)
		etiqSecretWord.config(fg="#ffffff", bg="#02290A")

		guessDisplay = tk.Entry(fr, textvariable=blanks, font=("Lucida Calligraphy", 18))
		guessDisplay.place(x=380, y=80)
		guessDisplay.config(width=35, background="black", fg="#9DEFAD", justify="center")

		#etiqCorrcLetters = tk.Label(listMision[mision], text="Correct Letters", font=("Lucida Calligraphy", 13))
		#etiqCorrcLetters.place(x=420, y=280)
		#etiqCorrcLetters.config(bg="#944DBD")

		#displCorrcLetters = tk.Entry(listMision[mision], textvariable=correctLettersDsp, font=("Arial", 13))
		#displCorrcLetters.place(x=350, y=310)
		#displCorrcLetters.config(width=35, background="black", fg="yellow", justify="center")

		etiqMissLetters = tk.Label(fr, text="Missed Letters", font=("Comic Sans MS", 13) )
		etiqMissLetters.place(x=620, y=130)
		etiqMissLetters.config(fg="#ffffff", bg="#02290A")

		displMissLetters = tk.Entry(fr, textvariable=missedLetters, font=("Arial", 13))
		displMissLetters.place(x=515, y=170)
		displMissLetters.config(width=35, background="black", fg="green", justify="center")

		etiqScore = tk.Label(fr, text="Score", font=("Lucida Calligraphy", 20))
		etiqScore.place(x=335, y=360)
		etiqScore.config(fg="#ffffff", bg="#02290A")

		displScore = tk.Label(fr, textvariable=score, font=("Arial", 34))
		displScore.place(x=295, y=400)
		displScore.config(background="black", fg="#9DEFAD", justify="center", width=6)

		btMeans = tk.Button(fr, image=graphic, command=lambda:tree_graphics())
		btMeans.config(fg="green")
		btMeans.place(x=490, y=240)

		btUse = tk.Button(fr, image=imnUse, command=lambda:exampleUse())
		btUse.place(x=610, y=240)

		btCoin = tk.Button(fr, image=coinbatt, command=lambda:explicCoins())
		btCoin.place(x=730, y=240)

		leyendCoin = tk.Label(fr, bg="white", fg="#FFD700", font=("Comic Sans MS", 10, "bold"))
		leyendCoin.place(x=735, y=245)
		leyendCoin.config(text=goldCoins)

		btGem = tk.Button(fr, image=gembatt, command=lambda:expplicGems())
		btGem.config(bg="#ffffff")
		btGem.place(x=840, y=240)

		displGems = tk.Label(fr, textvariable=lifesAc, font=("Comic Sans MS", 10))
		displGems.place(x=845, y=245)
		displGems.config(fg="blue")

		btFinish = tk.Button(fr, text="Finish riddle", font=("Comic Sans MS", 11), command=lambda:finishMision())
		btFinish.config(fg="green")
		btFinish.place(x=280, y=475)

		btquitP = tk.Button(fr, text="Quit game", font=("Comic Sans MS", 11), command=lambda:quitMision())
		btquitP.config(fg="green")
		btquitP.place(x=390, y=475)

		kali888 = tk.Label(fr, image = kali)
		kali888.place(x=20, y=20)

		


	elif language == "":

		messagebox.showinfo(parent=raiz, message = "You must choose a language first")


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

	text_cipher_var = tk.StringVar(value=cipherText_nbk1_jg[12])

	message = text_cipher_var.get()

	return message


def getKey_nbk1():

	global keyInput
	
	key = int(keyInput.get())

	return key



def getTranslatedMessage(mode, message, key):

	global cipher
	global keys_nbk1_jg

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

			text_cipher_var.get()

			text_cipher_var.set(text_cipher_var.get()[:y] + chr(num))
			#cipher.config(justify="center")

		else:

			symbol = message[y]

			text_cipher_var.get()

			text_cipher_var.set(text_cipher_var.get()[:y] + symbol)

		# 	#translated += symbol
	 		

		y = y + 1

	if key != keys_nbk1_jg[12]:

		time.sleep(2)
		text_cipher_var.set(cipherText_nbk1_jg[12])


conteo = 0

def tree_graphics():

	global conteo
	global tree_photos_jg
	global indice

	raiz = tk.Toplevel()
	raiz.title("TREE CODE")
	raiz.resizable(0,0)
	#raiz.geometry("650x350")
	marcoPresnt = tk.Frame(raiz)
	marcoPresnt.pack()

	x = 0
	crtPlayersonido = "createPlayer.wav"

	pantallas = tk.PhotoImage(file = tree_photos_jg[indice][0])
	#prim_pantalla = tk.PhotoImage(file="Primera_pantalla5.png")
	#seg_pantalla = tk.PhotoImage(file="Acacia_rubiniaesc.png")
	Presentacion = tk.Label(marcoPresnt, image=pantallas)
	Presentacion.pack()

	but = tk.Button(marcoPresnt, text = 'Change', command = lambda:changes())
	but.place(x=10, y=10)



	def changes():

		global conteo
		global pantallas
		global indice

		#grupo = tree_photos_jg

		playsound(crtPlayersonido)
		pantallas = tk.PhotoImage(file = tree_photos_jg[indice][conteo + 1])
		Presentacion.config(image=pantallas)
		but.config(text="Cambia")
		conteo = conteo + 1


		if conteo == len(tree_photos_jg[indice]) - 1:

			conteo = -1

	raiz.mainloop()


	

def quitMision():

	conexion2 = sqlite3.connect("players")
	cursor2 = conexion2.cursor()

	sql4 = "update playeridiom set (gems, goldcoins, score, gemsgand) = (?, ?, ?, ?) where nickname = (?)"
	datsActs = (lifesAc.get(), goldCoins, score.get(), gemsGanadas, nickname.get())

	cursor2.execute(sql4, datsActs)
	conexion2.commit()
	conexion2.close()

	raiz.destroy()



def jim():

	playsound(jimmy_en)
	playsound(jimmy_es)



# def explicCoins():

# 	playsound(frag)

def expplicGems():

	playsound(frag)





def finishMision():

	global words
	global idiomMeans
	global indice
	global listMision
	global mision 
	global idiomExamples

	if guessSecWord:

		#del idiomMeans[indice]
		#del idiomExamples[indice]
		del spanish_name_jg[indice]
		del english_name_jg[indice]
		del scientific_name_jg[indice]
		del tree_photos_jg[indice]

		conexion2 = sqlite3.connect("players")
		cursor2 = conexion2.cursor()

		sql4 = "update playeridiom set (gems, goldcoins, score, gemsgand) = (?, ?, ?, ?) where nickname = (?)"
		datsActs = (lifesAc.get(), goldCoins, score.get(), gemsGanadas, nickname.get())

		cursor2.execute(sql4, datsActs)
		conexion2.commit()
		conexion2.close()

		listMision[mision].destroy()

	
		


def exampleUse():

	global exceUse
	global idiomExamples

	if guessSecWord == False:

		playsound(exceUse)

	else:

		playsound(idiomExamples[indice])


conteo = 0



	
	

def letraPulsada(letra):
	global blanks
	global secretWord
	global correctLetters
	global correctLettersDsp
	global alreadyLetters
	global score
	global scoreAcumulado
	global wrongs
	global lifes
	global guessSecWord
	global passedMissions
	global runOut
	global ganancia
	global perdida
	global gameOver
	global avisoRunOut
	global goldCoins
	global leyendCoin
	global lifesAc
	global marcoAhorc

	for i in range(len(secretWord)):
		
		if letra in secretWord[i] and correctLetters < len(secretWord) and alreadyLetters.count(letra) < secretWord.count(letra) and wrongs <= 4:
			blanks.set(blanks.get()[:i] + secretWord[i] + blanks.get()[i+1:])
			correctLettersDsp.set(correctLettersDsp.get() + "   " + letra)
			correctLetters = correctLetters + 1
			alreadyLetters = alreadyLetters + letra
			score.set(score.get() + int((100/len(secretWord))))
			scoreAcumulado = scoreAcumulado + int((100/len(secretWord)))
			playsound(ganancia)
			

		
	if letra not in secretWord and correctLetters < len(secretWord) and wrongs <= 4:
		missedLetters.set(missedLetters.get() + "   " + letra)
		score.set(score.get() - 5)
		scoreAcumulado = scoreAcumulado - 5
		wrongs = wrongs + 1
		playsound(perdida)
		

	if correctLetters == len(secretWord):

		score.set(score.get() + 80)
		scoreAcumulado = scoreAcumulado + 80
		guessSecWord = True
		passedMissions = mision
		goldCoins = goldCoins + 1
		playsound(ganarPantalla)

		

		correctLetters = correctLetters + 1

	if wrongs >= 5 and lifes >= 1:

		runOut = True
		lifes = lifes - 1
		lifesAc.set(lifesAc.get() - 1)
		wrongs = 0

		

		if avisoRunOut == 1:

			avisoRunOut = 0

		#marcoAhorc.config(image=Verd2)

	elif wrongs >= 5 and lifes == 0:

		runOut = True		
		gameOver = True
		lifes = lifes - 1
		lifesAc.set(lifesAc.get() - 1)

		if avisoRunOut == 1:

			avisoRunOut = 0


	#leyendCoin.config(text=goldCoins)

def messagesFail():

	if lifes == 3:

		playsound(frag)

def resetCrLetters():
	global correctLetters
	global alreadyLetters
	global wrongs
	global guessSecWord
	global passedMissions
	global mision
	global avisoGuess
	global words
	global idiomMeans
	global indice

	if passedMissions == mision and nickname.get() != "" and lifes >= 0:

		correctLetters = 0
		alreadyLetters = ""
		wrongs = 0
		guessSecWord = False
		avisoGuess = 0
		

	elif passedMissions < mision and lifes >= 0:

		messagebox.showinfo(parent=raiz, message= "You must guess the current secret idiom first")

	elif nickname.get() == "":

		messagebox.showinfo(parent=raiz, message = "You must activate a player first")

	elif nickname.get() != "" and lifes < 0:

		playsound(playerHasNoGems)



def guessSecretWord():
	
	global guessSecWord
	global avisoGuess
	global gemsGanadas
	global goldCoins
	global lifes
	global lifesAc

	if guessSecWord and avisoGuess == 0:
		messagebox.showinfo(parent = listMision[mision], message = ("Well done!! you have guessed the secret idiom:  " + secretWord), title="Idioms Code")
		

		avisoGuess = 1

		if gemsGanadas < goldCoins//10:

			lifes = lifes + 1
			lifesAc.set((lifesAc.get()) + 1)
			gemsGanadas = gemsGanadas + 1
			playsound(premGem)


def runOutGuess():

	global runOut
	global avisoRunOut
	global marcoAhorc

	if runOut and avisoRunOut == 0 and gameOver == False:
		messagebox.showinfo(parent = listMision[mision], message = "You are run out of guesses. You have actually guessed: " + str(mision) + " idioms.\nTry again.", title="Idioms Code")
		avisoRunOut = 1
		runOut = False
		marcoAhorc.config(image=Verd2, bg="#02290A")
		playsound(risaJim)
		playsound(gemLostt)
		

	elif runOut and avisoRunOut == 0 and gameOver:
		
		messagebox.showinfo(parent = listMision[mision], message = "The game is over. You have guessed " + str(mision) + " idioms", title="Idioms Code")
		avisoRunOut = 2
		playsound(risaFin)
		conexion2 = sqlite3.connect("players")
		cursor2 = conexion2.cursor()

		sql4 = "update playeridiom set (gems, goldcoins, score, gemsgand) = (?, ?, ?, ?) where nickname = (?)"
		datsActs = (lifesAc.get(), goldCoins, score.get(), gemsGanadas, nickname.get())

		cursor2.execute(sql4, datsActs)
		conexion2.commit()
		conexion2.close()
		listMision[mision].destroy()



# buttonExample = tk.Button(raiz, 
# 			  text="Create Riddle", font=("Comic Sans MS", 12), fg="blue", command=lambda:[resetCrLetters(), createNewWindow()])
# buttonExample.place(x=620, y=480)



#botonCambImg = tk.Button(raiz, text="cambiar", command=lambda:cambiarImagen())
#botonCambImg.place(x=520, y=480)



raiz.mainloop()