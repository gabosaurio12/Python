#Import
from tkinter import*
import tkinter.messagebox
from tkinter import ttk

#Base of the window
win=Tk()
win.title("Tabla de decisiones")
win.geometry("1000x200")
win.config(bg="black")
win.resizable(0,0)
win.iconbitmap("volley.ico")

#The Frame  ------→ Buttons, images
mfra=Frame(win)
mfra.config(bg="black")
mfra.pack()

#Label

tit=Label(mfra, text="Tabla de decisiones",bg="black", fg="white", font=("Comic Sans ms",24))
tit.grid(row=0, column=2, columnspan=4)

blolab=Label(mfra, text="Bloqueadores", bg="black", fg="white", font=("Comic Sans ms",12))
blolab.grid(row=1,column=1)

tipblolab=Label(mfra, text="Tipo de bloqueo", bg="black", fg="white", font=("Comic Sans ms",12))
tipblolab.grid(row=1,column=2)

paslab=Label(mfra, text="Pase", bg="black", fg="white", font=("Comic Sans ms",12))
paslab.grid(row=1,column=3)

reclab=Label(mfra, text="Receptores", bg="black", fg="white", font=("Comic Sans ms",12))
reclab.grid(row=1,column=4)

acclab=Label(mfra, text="Mejor Acción", bg="black", fg="white", font=("Comic Sans ms",12))
acclab.grid(row=1,column=5)

#----------Buttons----------#

def insbut():
	tkinter.messagebox.showinfo("Instrucciones de uso","En -Bloqueadores- escribir SOLO CON NÚMERO la cantidad de bloqueadores, en -Tipo de bloqueo- escribir si es -Ofensivo- o -Defensivo-, en -Pase- escribir si es -Bueno- o -Malo-, en -Receptores- escribir si la recepción -Corta- o -larga- y en Mejor Acción aparecerá la mejor opción de acción")

def posbut():
    novi=Toplevel()
    canvas=Canvas(novi, width = 400, height = 600)
    canvas.config(bg="#00CCCC")
    canvas.pack(expand = YES, fill = BOTH)
    imcan=PhotoImage(file = 'posiciones.png')
    canvas.create_image(50, 10, image=imcan, anchor = NW)
    canvas.imcan=imcan

def actbut():
	tkinter.messagebox.showinfo("Acciones","""
	Remate: Pégale con ganas.
	Dejada: Toque de dedos.
	Roce: Remate a los dedos de los bloqueadores.
	Roce corto: Remate al borde de un bloqueo, buscando que rebote hacía afuera.
	Rebote: Cáscara hacia los dedos de los bloqueadores para que sea posible recuperar el balón.
	Cáscara: Roce al balón haciendo el gesto del remate, dándole fuerza con la muñeca, para que lleve mucho giro.""")

#-----------Actions-----------#
def entbut():
	try:
		a=(bl.get()).lower() #Bloqueadores
		b=(tbl.get()).lower() #Tipo de bloqueo
		c=(pse.get()).lower() #Pase
		d=(rcp.get()).lower() #Tipo de receptores

		if a=="1":
			if b=="defensivo":
				if c=="malo":
					if d=="corta":
						mejac.set("Rebote")
					elif d=="larga":
						mejac.set("Dejada a 8")
				elif c=="bueno":
					if d=="corta":
						mejac.set("Remate a 5")
					elif d=="larga":
						mejac.set("Remate a 7")
			elif b=="ofensivo":
				if c=="malo":
					if d=="corta":
						mejac.set("Dejada a 1")
					elif d=="larga":
						mejac.set("Dejada a 8")
				elif c=="bueno":
					if d=="corta":
						mejac.set("Remate a 1")
					elif d=="larga":
						mejac.set("Remate a 9")

		elif a=="2":
			if b=="defensivo":
				if c=="malo":
					if d=="corta":
						mejac.set("Rebote")
					elif d=="larga":
						mejac.set("Dejada a 8")
				elif c=="bueno":
					if d=="corta":
						mejac.set("Remate a 1")
					if d=="larga":
						mejac.set("Remate a 7")

			elif b=="ofensivo":
				if c=="malo":
					if d=="corta":
						mejac.set("Dejada a 1")
					elif d=="larga":
						mejac.set("Dejada a 8")
				elif c=="bueno":
					if d=="corta":
						mejac.set("Remate largo")
					elif d=="larga":
						mejac.set("Roce corto")

		elif a=="3":
			if b=="defensivo":
				if c=="malo":
					if d=="corta":
						mejac.set("Rebote")
					elif d=="larga":
						mejac.set("Dejada a 8")
				elif c=="bueno":
					if d=="corta":
						mejac.set("Remate diagonal largo")
					if d=="larga":
						mejac.set("Cáscara a 8")

			elif b=="ofensivo":
				if c=="malo":
					if d=="corta":
						mejac.set("Dejada a 1")
					elif d=="larga":
						mejac.set("Dejada a 8")
				elif c=="bueno":
					if d=="corta":
						mejac.set("Remate largo")
					elif d=="larga":
						mejac.set("Cáscara")

	except ValueError:
		pass

#Buttons

butinst=Button(mfra, text="Instrucciones", bg="black", fg="white", font=("Comic Sans ms", 12), command=insbut)
butinst.grid(row=0, column=1)

butpos=Button(mfra, text="Posiciones", bg="black", fg="white", font=("Comic Sans ms", 12), command=posbut)
butpos.grid(row=0, column=6)

butres=Button(mfra, text="Enter", bg="black", fg="white", font=("Comic Sans ms",12), command=entbut)
butres.grid(row=0, column=7)

butacc=Button(mfra, text="Acciones", bg="black", fg="white", font=("Comic Sans ms",12), command=actbut)
butacc.grid(row=3, column=1)

#Entry

bl=StringVar()
bloq=Entry(mfra, textvariable=bl, bg="black", fg="white")
bloq.grid(row=2, column=1)

tbl=StringVar()
tipblo=Entry(mfra, textvariable=tbl, bg="black", fg="white")
tipblo.grid(row=2, column=2)

pse=StringVar()
pase=Entry(mfra, textvariable=pse, bg="black", fg="white")
pase.grid(row=2, column=3)
rcp=StringVar()
rec=Entry(mfra, textvariable=rcp, bg="black", fg="white")
rec.grid(row=2, column=4)

mejac=StringVar()
ttk.Label(mfra, textvariable=mejac, foreground="white", background="black").grid(row=2, column=5)

#Mainloop

win.mainloop()