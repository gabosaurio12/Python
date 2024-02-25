from tkinter import *
import os

#root

root = Tk()
root.geometry("1080x650")
root.resizable(0,0)
root.config(bg = "black")

#main_frame
main_frame = Frame(root)
main_frame.config(bg = "black", width = 1080, height = 650)
main_frame.pack()

#fotos y fondo principal

foto_fondo = PhotoImage(file = "fondo.png")

foto_fondo_prosettings = PhotoImage(file = "pro.png")

fondo_principal = Label(main_frame, image = foto_fondo, bg = "black").grid(row = 0, column = 0, columnspan = 40, rowspan = 40)

#titulo

title = Label(main_frame, text = "ENCICLOPEDIA DE VALORANT", bg = "#0D6360", fg = "red", font = ("Arial",35)).grid(row = 0, column = 1, pady = 15)

#Equipos 


#boton de prosettings

def pro_settings():
	fondo_de_prosettings = Label(main_frame, image = foto_fondo_prosettings, bg = "black").grid(row = 1, column = 0, columnspan = 40, rowspan = 40)

	tarik = Label(main_frame, text = "Tarik", bg = "#872424", fg = "white", font = ("Arial", 24)).grid (row = 2 , column = 0, columnspan = 2) #podria ser buena idea hacer la imagen

#Quit

def quit():
	exit

#Calculadora

def btn_calc():
	input_dpi=StringVar()
	input_sens=StringVar()
	input_result=StringVar()

	entry_dpi=Entry(main_frame,bd=0,bg="black", fg="White",width=25, textvariable=input_dpi, borderwidth=5, justify=RIGHT).grid(row=3, column=1)
	intdpi=Label(main_frame, text="Introduce tu DPI", foreground="white", background="black").grid(row=3, column=0)

	entry_sens=Entry(main_frame,bd=0,bg="black", fg="White",width=25, textvariable=input_sens, borderwidth=5, justify=RIGHT).grid(row=4, column=1)
	intsens=Label(main_frame, text="Introduce tu Sens", foreground="white", background="black").grid(row=4, column=0)

	def caledpi():
		adpi = float(input_dpi.get())
		asens = float(input_sens.get())
		operedpi = adpi*asens
		result=Label(main_frame, text=operedpi, background="black", foreground="White").grid(row=5, column=1)

	btn_edpi=Button(main_frame, text="Calcular EDPI", width="20", height="2", fg="white", bg="black", command=lambda:caledpi()).grid(row=5, column=0, pady=5)

#Botones

boton_prosettings=Button(main_frame, text="ProSettings", width="20", height="2", fg="white", bg="black", command=lambda: pro_settings()).grid(row=1, column=0, pady=5)

boton_calc_de_edpi=Button(main_frame, text="Calculadora de EDPI", width="20", height="2", fg="white", bg="black", command=lambda: btn_calc()).grid(row=1, column=1, pady=5)

salir=Button(main_frame, text="Salir", width="20", height="2", fg="white", bg="black", command=lambda:exit()).grid(row=1, column=2, pady=5)

root.mainloop()