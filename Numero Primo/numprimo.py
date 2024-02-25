num = int(input("Ingresa un numero "))

i = 2;
band = True
while band and i<num :
    primo = num % i
    if primo == 0:
        band = False
    i = i + 1

if band:
    print ("Es primo")
else:
    print ("No es primo")

