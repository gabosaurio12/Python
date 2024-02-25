from tkinter import*

root = Tk()
root.config(bg="black")
root.geometry("350x200")
root.resizable(0, 0)
root.title("Calculadora")

titulo = Label(root, text="Calculadora", bg="black", fg="white")
titulo.grid(column=1, row=0)
etiquetaN1 = Label(root, text="Numero", bg="black", fg="white")
etiquetaN1.grid(column=0, row=1)
etiquetaN2 = Label(root, text="Numero", bg="black", fg="white")
etiquetaN2.grid(column=0, row=2)
etiquetaRes = Label(root, text="Resultado", bg="black", fg="white")
etiquetaRes.grid(column=0, row=3)

num1 = StringVar()
num2 = StringVar()

entry1 = Entry(root, bg="black", fg="white", textvariable=num1)
entry1.grid(column=1, row=1)
entry2 = Entry(root, bg="black", fg="white", textvariable=num2)
entry2.grid(column=1, row=2)

etRes = Label(root, bg="black", fg="white", text=" ")
etRes.grid(column=1, row=3)

def FuncionSuma():
    a = float(num1.get())
    b = float(num2.get())
    resultado = a + b
    etRes.config(text=resultado)

def FuncionResta():
    a = float(num1.get())
    b = float(num2.get())
    resultado = a - b
    etRes.config(text=resultado)

def FuncionDiv():
    a = float(num1.get())
    b = float(num2.get())
    resultado = a / b
    etRes.config(text=resultado)

def FuncionMult():
    a = float(num1.get())
    b = float(num2.get())
    resultado = a * b
    etRes.config(text=resultado)

def clear():
    limpio = " "
    etRes.config(text=limpio)

botonSuma = Button(root, text="Suma", bg="black", fg="white", width=10, command=FuncionSuma)
botonSuma.grid(column=1, row=4)
botonResta = Button(root, text="Resta", bg="black", fg="white", width=10, command=FuncionResta)
botonResta.grid(column=2, row=4)
botonDiv = Button(root, text="Division", bg="black", fg="white", width=10, command=FuncionDiv)
botonDiv.grid(column=1, row=5)
botonMult = Button(root, text="Multiplicacion", bg="black", fg="white", width=10, command=FuncionMult)
botonMult.grid(column=2, row=5)
botonDel = Button(root, text="C", bg="black", fg="white", width=10, command=clear)
botonDel.grid(column=2, row=6)

root.mainloop()