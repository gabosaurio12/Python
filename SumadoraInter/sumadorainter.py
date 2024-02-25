from tkinter import*

root = Tk();
root.title("Sumadora Tkinter")
root.geometry ("300x150")
root.resizable(0,0)
root.config (bg = "Dark blue")

num1 = StringVar()
num2 = StringVar()

titulo = Label (root, text = "Sumadora con Tkinter", bg = "Dark blue", fg = "white").grid(column = 1, row = 0)
etiqueta1 = Label (root, text = "Numero 1", bg = "Dark blue", fg = "White").grid (column = 0, row = 1)
entrada1 = Entry(root, textvariable = num1).grid (column = 1, row = 1)

etiqueta2 = Label (root, text = "Numero 2", bg = "Dark blue", fg = "White").grid (column = 0, row = 2)
entrada2 = Entry (root, textvariable = num2).grid (column = 1, row = 2)

def mostrarRes():
    a = float (num1.get())
    b = float (num2.get())
    suma = a + b
    resultado = Label (root, text = suma, bg = "Dark blue", fg = "Light green").grid (column = 1, row = 3)

etiquetaresultado = Label (root, text = "Resultado", bg = "Dark blue", fg = "White").grid (column = 0, row = 3)
boton = Button (root, text = "Enter", bg = "Dark blue", fg = "White", command = lambda: mostrarRes()).grid (column = 1, row = 4)


root.mainloop()
