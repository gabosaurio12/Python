from tkinter import*

Ventana=Tk() 
Ventana.title("Fonda de Gabo-Sama")
Ventana.geometry("800x800")
Ventana.resizable(0,0)
Ventana.config(bg="#1affff")

imagen_tamales=PhotoImage(file="Tamales 2.png")
texto_tamales="El tamal es un alimento de origen mesoamericano preparado generalmente a base de masa de maíz rellena de carnes, vegetales, chiles, frutas, salsas y otros ingredientes.Precio de un tamal:$15.​​"
imagen_gorditas=PhotoImage(file="Gorditas2.png")
texto_gorditas="Son hechas con frijoles salsa roja o salsa verde, las gorditas son hechas a mano.Precio de una orden(5 gorditas):$15."
imagen_tostadas=PhotoImage(file="Tostadas2.png")
texto_tostadas="Es una tortilla tostada con mayonesa,jamón,lechuga,queso,pollo,crema,tomate y chiles.Precio de una orden(2 tostadas grandes):$50."
imagen_coca=PhotoImage(file="Coca2.png")
texto_coca="Esta es una bebida gaseosa, refrescante pero dulce, se dice que quita el dolor de cabeza.Precio 500ml:$10."
imagen_agua=PhotoImage(file="Agua2.png")
texto_agua="Una deliciosa y refrescante agua natural.Precio:$5."
imagen_limon=PhotoImage(file="Limón2.png")
texto_limon="Una refrescante agua de limón con limones frescos sic saborizantes.Precio del vaso:$20.Precio de la jarra:$25."






def boton_borrar():
	area_de_texto.delete(1.0,END)
	pantalla.delete(ALL)
def tamal():
	pantalla.delete(ALL)
	pantalla.create_image(150,150, image=imagen_tamales,tags="Tamales")
	area_de_texto.insert(INSERT,texto_tamales)
def boton1():
	pantalla.delete(ALL)
	pantalla.create_image(150,150,image=imagen_tamales,tags="Tamales")
	area_de_texto.insert(INSERT,texto_tamales)

def gorditas():
	pantalla.delete(ALL)
	pantalla.create_image(150,150, image=imagen_gorditas,tags="Gorditas")
	area_de_texto.insert(INSERT,texto_gorditas)
def boton2():
	pantalla.delete(ALL)
	pantalla.create_image(150,150,image=imagen_gorditas,tags="Gorditas")
	area_de_texto.insert(INSERT,texto_gorditas)
def tostadas():
	pantalla.delete(ALL)
	pantalla.create_image(150,150, image=imagen_tostadas,tags="Tostadas")
	area_de_texto.insert(INSERT,texto_gorditas)
def boton3():
	pantalla.delete(ALL)
	pantalla.create_image(150,150,image=imagen_tostadas,tags="Tostadas")
	area_de_texto.insert(INSERT,texto_tostadas)
def coca():
	pantalla.delete(ALL)
	pantalla.create_image(150,150, image=imagen_coca,tags="Coca-cola")
	area_de_texto.insert(INSERT,texto_coca-cola)
def boton4():
	pantalla.delete(ALL)
	pantalla.create_image(150,150,image=imagen_coca,tags="Coca-cola")
	area_de_texto.insert(INSERT,texto_coca)
def agua():
	pantalla.delete(ALL)
	pantalla.create_image(150,150,image=imagen_agua,tags="Agua")
	area_de_texto.insert(INSERT,texto_agua)
def boton5():
	pantalla.delete(ALL)
	pantalla.create_image(150,150,image=imagen_agua,tags="Agua")
	area_de_texto.insert(INSERT,texto_agua)
def limon():
	pantalla.delete(ALL)
	pantalla.create_image(150,150,image=imagen_limon,tags="Limón")
	area_de_texto.insert(INSERT,texto_limon)
def boton6():
	pantalla.delete(ALL)
	pantalla.create_image(150,150,image=imagen_limon,tags="Limón")
	area_de_texto.insert(INSERT,texto_limon)





area_de_texto=Text(Ventana,height=11, width=57,padx=5,pady=5)
area_de_texto.grid(column=0,row=100,columnspan=2)


pantalla=Canvas(Ventana,width=300,height=300)
pantalla.grid(column=1,row=0,rowspan=4)

boton1=Button(Ventana,text="Tamales",width=20,command=boton1,bg="#b32400")
boton1.grid(column=0,row=1,padx=20)

boton_borrar=Button(Ventana,text="Borrar",width=20,command=boton_borrar,bg="#ff0000")
boton_borrar.grid(column=0,row=0,padx=20)

boton2=Button(Ventana,text="Gorditas",width=20,command=boton2,bg="#b32400")
boton2.grid(column=0,row=2,padx=20)

boton3=Button(Ventana,text="Tostadas",width=20,command=boton3,bg="#b32400")
boton3.grid(column=0,row=3,padx=20)

boton4=Button(Ventana,text="Coca-cola",width=20,command=boton4,bg="#b3ffb3")
boton4.grid(column=0,row=4,padx=20)

boton5=Button(Ventana,text="Agua",width=20,command=boton5,bg="#b3ffb3")
boton5.grid(column=0,row=5,padx=20)

boton6=Button(Ventana,text="Limón",width=20,command=boton6,bg="#b3ffb3")
boton6.grid(column=0,row=6,padx=20)












































































Ventana.mainloop()
