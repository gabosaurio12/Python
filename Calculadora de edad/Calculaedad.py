#Función interfaz
def inter():
    p1=input('¿Quiéres usar la fecha actual? ').lower()
    if p1=='si':
        fact()
    elif p1=='no':
        fesp()

#Función de fecha actual
def fact():
    #Fecha de nacimiento
    a=int(input('¿Qué día naciste? '))
    b=int(input('¿Qué mes naciste? '))
    c=int(input('¿En qué año naciste? '))

    #biblioteca de fecha
    from datetime import date
    from datetime import datetime
    fec=date.today()

    #Fecha
    di=fec.day
    me=fec.month
    añ=fec.year

    #Calcular la diferencia
    edadia=di-a
    edames=me-b
    edaño=añ-c

    #Calculando la edad
    if edadia<0 or edames<0:
        print(edaño-1)
    elif edadia>=0 or edames>=0:
        print(edaño)
  
    #Repetición
    rep=input('¿Quiéres calcular otra edad? ').lower()
    if rep=='si':
        inter()
    elif rep=='no':
        sal=input('¿Gustas salir? ').lower()
        if sal=='si':
            print('Que tengas un excelente día, ¡nos vemos!')
            import sys
            sys.exit()
        elif sal=='no':
            print('¿Qué quiéres de mi?')
            import sys
            sys.exit()

#Fecha específica
def fesp():
    #Fecha
    print('Deberás ingresar las fecha que quieres comparar')
    j=int(input('¿Qué día quiéres usar? '))
    k=int(input('¿Qué mes quiéres usar? '))
    l=int(input('¿Qué añño quiéres usar? '))

    #Nacimiento
    print('Deberás ingresar la fecha de nacimiento')
    p=int(input('¿Qué día naciste? '))
    q=int(input('¿En qué mes naciste? '))
    x=int(input('¿En qué año naciste? '))

    #Calcula diferencia
    edadias=j-p
    edadmes=k-q
    edaños=l-x

    #Calculando la edad
    if edadias<0 or edadmes<0:
        if edaños<0:
            print('Aún no nacías, ¿O acaso eres un viajero en el tiempo?...')
        elif edaños>=0:
            print(edaños-1)
    elif edadias>=0 or edadmes>=0:
        print(edaños)
        
    
    #Repetición
    rep=input('¿Quiéres calcular otra edad? ').lower()
    if rep=='si':
        inter()
    elif rep=='no':
        sal=input('¿Gustas salir? ').lower()
        if sal=='si':
            print('Que tengas un excelente día, ¡nos vemos!')
            import sys
            sys.exit()
        elif sal=='no':
            print('¡¿Qué quiéres de mi?!')
            print('¡ADIÓS MUNDO CRUEL!')
            import sys
            sys.exit()


#Interfaz
print('Hola soy una calculadora de edad')
inter()