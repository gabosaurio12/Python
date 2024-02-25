from tkinter import*

root = Tk()
root.config(bg = "Black")
root.geometry("350x200")
root.resizable(0,0)
root.title("Calculadora")

titulo = Label (root, 
                text = "Calculadora", 
                bg = "Black", fg = "White")
titulo.grid (column = 1, row = 0)
etiquetaN1 = Label (root, 
                text = "Numero", 
                bg = "Black", fg = "White")
etiquetaN1.grid (column = 0, row = 1)
etiquetaN2 = Label (root, 
                text = "Numero", 
                bg = "Black", fg = "White")
etiquetaN2.grid (column = 0, row = 2)
etiquetaRes = Label (root, 
                text = "Resultado", 
                bg = "Black", fg = "White")
etiquetaRes.grid (column = 0, row = 3)

num1 = StringVar()
num2 = StringVar()

entry1 = Entry (root, 
                bg = "Black", fg = "White", 
                textvariable = num1
                ).grid (column = 1, row = 1)
entry2 = Entry (root, 
                bg = "Black", fg = "White", 
                textvariable = num2)
entry2.grid (column = 1, row = 2)
etRes = Label(root, 
              bg = "Black", fg = "White", 
              text = " ")
etRes.grid(column = 1, row = 3)

def FuncionSuma():
    a = float(num1.get())
    b = float(num2.get())
    resultado = a + b
    etRes.config(text = " ")
    etRes.config(text = resultado)
    
def FuncionResta():
    a = float(num1.get())
    b = float(num2.get())
    resultado = a - b
    etRes.config(text = " ")
    etRes.config(text = resultado)

def FuncionDiv():
    a = float(num1.get())
    b = float(num2.get())
    resultado = a / b
    etRes.config(text = " ")
    etRes.config(text = resultado)

def FuncionMult():
    a = float(num1.get())
    b = float(num2.get())
    resultado = a * b
    etRes.config(text = " ")
    etRes.config(text = resultado)

def clear():
    limpio = " "
    etRes.config (text = limpio)

botonSuma = Button (root, 
        text = "Suma", 
        bg = "Black", fg = "White", width = 10, 
        command = lambda : FuncionSuma()
        ).grid (column = 1, row = 4)
botonResta = Button (root, 
        text = "Resta", 
        bg = "Black", fg = "White", width = 10, 
        command = lambda : FuncionResta()
        ).grid (column = 2, row = 4)
botonDiv = Button (root, 
        text = "Division", 
        bg = "Black", fg = "White", width = 10, 
        command = lambda : FuncionDiv()
        ).grid (column = 1, row = 5)
botonMult = Button (root, 
        text = "Multiplicacion", 
        bg = "Black", fg = "White", width = 10, 
        command = lambda : FuncionMult()
        ).grid (column = 2, row = 5)


root.mainloop()
