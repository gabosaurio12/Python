print("Hola, cual es tu nombre? ") #con print imprimes cosas en pantalla
nombre = input(); #con input lees informacion
print("Mucho gusto ", nombre)
print("#Esta es la primera pregunta que tendra un error")
pregunta = input("Te gusta Tay Tay? ") #puedes incluir texto dentro del input

if pregunta == "si": #la estructura del SI es if expresion :
    print("Me caes bien")
else: #el else es igual que en C++
    print("No me caes tan bien")

#En el if de arriba tenemos el inconveniente de que si escriben "Si" o "SI" o "sI" ya no le caeremos tan bien, para esto tenemos
#la funcion .lower() y .upper()

#primero me gustaria explicar como se hacen funciones en python
#aca para hacer una funcion se usa el comando def nombre ():

def pregunta1(): #esta funcion transforma el texto que ingreses en mayusculas
    pregunta = input("Te gusta Tay Tay? ").upper()
    return pregunta

def pregunta2(): #esta funcion transforma el texto que ingreses en minusculas
    pregunta = input("Te gusta Tay Tay? ").lower()
    return pregunta
    
def pregunta3():
    pregunta = input("Te gusta Tay Tay? ").upper()
    return pregunta

#Estas son las siguientes preguntas que no tendran error
print("#Pregunta si o no upper()")
rMay = pregunta1()
print("#Pregunta si o no lower()")
rMin = pregunta2()
print("#Pregunta mas o menos")
respuesta = pregunta3()

print("#Imprimimos los resultados de las funciones")
print(rMay)
print(rMin)
print(respuesta)

print("#Rehacemos la pregunta")
if rMin == "si": #Ahora sin importar la forma en la que escriba "Si", le caeras bien
    print("Me caes bien")
else: #el else es igual que en C++
    print("No me caes tan bien")

#Selectivas multiples
#los elifs se usan para selectivas multiples, no es necesario anidar ifs
print("#Selectivas multiples")
if respuesta == "SI":
    print("Me caes muy bien!")
elif respuesta == "MAS O MENOS": #este elif solo se ejecutara si el primer if fue falso
    print("Me agradas")
elif respuesta == "NO": #Y este si el elif anterior fue falso
    print("No me caes bien")

#ciclos
print("#Ciclos")
i = 0 #se debe inicializar
while i < 5: #misma estructura que el if
    print(i)
    i = i + 1 #no olvides esto
    
b = int(input("B "))
for i in range(i, 8):
    print(i)

#operaciones

a = int(input("A "))
d = float(a)
b = float(input("B "))

c = b + d
print(c)
