from random import shuffle

#lista inicial
palitos = ["-","--","---","----"]

#mezcla de palitos
def mezclar_palitos(palitos):
    shuffle(palitos)
    return palitos

#pedir intento
def probar_suerte():
    intento = ''
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un palito un numero de 1-4: ")
    return int(intento)


#comprobar intento

def comprobar_intento(palitos, intento):
    if palitos[intento - 1] == "----":
        print("¡Felicidades! ¡Has ganado!")
    else:
        print("Lo siento, inténtalo de nuevo.")
        print(f"El palito elegido fue: {palitos[intento - 1]}")

comprobar_intento(mezclar_palitos(palitos), probar_suerte())