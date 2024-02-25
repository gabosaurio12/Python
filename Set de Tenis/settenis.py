a = int (input ("Ingresa el número de juegos ganado por el visitante "))
b = int (input ("Ingresa el número de juegos ganado por el local "))

if a == 7:
    print ("Ganó el visitante")
elif b == 7:
    print ("Ganó el local")
elif a < 7 and b < 7:
    print ("Aún no termina")
elif a >= 8  or b >= 8:
    print ("No es válido")
