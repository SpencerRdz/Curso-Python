from random import randint

nombre = "Spencer" # input
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

numero_programa = randint(1,100)
intentos = 0

while intentos < 8:
    numero_usuario = int(input("Ingresa un numero: "))
    intentos += 1
    if numero_usuario > 1 and numero_usuario < 100:
        if numero_usuario < numero_programa:
            print("su respuesta es incorrecta y que ha elegido un número menor al número secreto.")
        elif numero_usuario > numero_programa:
            print("su respuesta es incorrecta y que ha elegido un número mayor al número secreto.")
        elif numero_usuario == numero_programa:
            print(f"Felicidades {nombre} haz ganado, te tomó {intentos} conseguirlo ")
            break
    else:
        print("ha elegido un número que no está permitido.")

    continue

if numero_programa != numero_usuario:
    print(f"Tu numero secreto era: {numero_programa}")