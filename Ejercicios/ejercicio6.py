print("Ingresa un numero <0 para dejar de leer")

band = 1
suma = 0
c = 0

while band:
	n = int(input())
	if n > -1:
		suma = suma + n
		c+=1
	else:
		band = 0

print(suma / c)