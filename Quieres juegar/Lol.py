name=input("Hola, cómo te llamas? ")
print("Oh ya veo")
print("Mucho gusto ", name,"yo me llamo...")
print("sjfke")
print("hosifhs")
print("ñajgñjasfd")
print("""


""")
print("Perfecto, ya no nos interrumpirán")
print("Yo soy NON, un placer")

#Juego
def castigo():
    confir=input("Testigo, ya hizo el castigo?").lower()
    if confir=="ya":
        print("Perfecto")
        print("Si me mienten...")
        print("¡HABRÁ REPRESALIAS")
        reto()
    elif confir=="no":
        print("Pues...")
        print("¡¿QUÉ ESPERAN?!")
        print("¡HÁGANLO!")
        castigo()
        
def resp2():
    resp1=input("Cuál es la respuesta ").lower()
    if resp1 == "ambos ceden":
        print("Correcto")
        reto()
    elif resp1 !="ambos ceden":
        print("Agotaste mi paciencia")
        print("Debes hacer el castigo por incumplimiento")
        castigo()
        
def reto():
    print("El siguiente reto será físico")
    print("Haz 10 burpiees")
    retoconfir=input("Testigo, ya hizo el reto?").lower()
    if retoconfir=="ya":
        print("Muy bien")
        print("Si me llegan a engañar, y los descubro...")
        print("¡HABRÁ CONSECUENCIAS!")
        reto()
    elif retoconfir=="no":
        print("Pues...")
        print("¡¿QUÉ ESPERAN?!")
        print("¡HAZLO!")
        print("Como ya sabes")
        reto()
    
def acertijo():
    print("El primer reto es un acertijo")
    print("Qué pasa cuando el objeto imparable choca con el objeto inamovible.")
    resp1=input("Cuál es la respuesta ").lower()
    if resp1 == "ambos ceden":
        print("Correcto")
        reto()
    elif resp1 !="ambos ceden":
        print("Intenta otra vez")
        resp2()

def juego():
    print("""
Para empezar explicaré las reglas:
1.- Debes de cumplir, si no alguien sufrirá.
2.- Si no cumples debes hacer 20 lagartijas seguidas.
3.- Cumplir regla 1 y 2.
""")
    ready=input("Estás listo? ").lower()
    if ready=="si":
        acertijo()
    elif ready=="no":
        print("¡HARÁS LO QUE YO DIGA!")
        acertijo()


preg1=input("Quiéres jugar un juego? ").lower()
if preg1=="no":
    print("ERROR")
    print("Harás lo que yo diga")
    juego()
elif preg1=="si":
    print("PERFECTO")
    print("Respuesta correcta")
    juego()


