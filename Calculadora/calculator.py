from tkinter import*

#root
root=Tk()
root.config(bg="black")
root.resizable(0,0)
root.title("Calculadora")


#funciones

def bt_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

input_text=StringVar()

#entry

inpframe=Frame(root,background="black")
inpframe.pack(side=TOP)

barra=Entry(inpframe,bd=0,bg="black", fg="White",width=25, textvariable=input_text, justify=RIGHT)
barra.grid(row=0,column=0,columnspan=100)
barra.pack(ipady=10)

#buttons

btframe=Frame(root,background="black")
btframe.pack()

one=Button(btframe,text="1",bg="black",fg="white", activebackground="#303031", activeforeground="#00FF08", padx=20, pady=15, command=lambda:bt_click(1)).grid(row=1,column=0)

two=Button(btframe,text="2",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(2)).grid(row=1,column=1)

three=Button(btframe,text="3",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(3)).grid(row=1,column=2)

four=Button(btframe,text="4",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(4)).grid(row=2,column=0)

five=Button(btframe,text="5",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(5)).grid(row=2,column=1)

six=Button(btframe,text="6",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(6)).grid(row=2,column=2)

seven=Button(btframe,text="7",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(7)).grid(row=3,column=0)

eight=Button(btframe,text="8",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(8)).grid(row=3,column=1)

nine=Button(btframe,text="9",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(9)).grid(row=3,column=2)

zero=Button(btframe,text="0",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(0)).grid(row=4,column=1)

point=Button(btframe,text=".",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click(".")).grid(row=4,column=0)

plus=Button(btframe,text="+",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click("+")).grid(row=1,column=3)

minus=Button(btframe,text="-",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click("-")).grid(row=2,column=3)

mult=Button(btframe,text="x",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click("*")).grid(row=3,column=3)

div=Button(btframe,text="÷",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_click("/")).grid(row=4,column=3)

equal=Button(btframe,text="=",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=20,pady=15, command=lambda:bt_equal()).grid(row=4,column=2)

clear=Button(btframe,text="C",bg="black",fg="white",activebackground="#303031",activeforeground="#00FF08",padx=40,pady=15, command=lambda:bt_clear("C")).grid(row=5,column=0, columnspan=100)

#mainloop
root.mainloop()