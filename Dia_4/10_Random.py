from random import *

aleatorio = randint(1, 100) # genera un número entero aleatorio entre 1 y 100
print(aleatorio)

aleatorio = round(uniform(1.0, 10.0),2) # genera un número flotante aleatorio entre 1.0 y 10.0 y lo redondea a 2 decimales
print(aleatorio)

aleatorio = round(random()) # genera un número flotante aleatorio entre 0.0 y 1.0
print(aleatorio)

choices = ['piedra', 'papel', 'tijera']
aleatorio = choice(choices) # selecciona un elemento aleatorio de la lista
print(aleatorio)

numeros = [1, 2, 3, 4, 5]
shuffle(numeros) # mezcla la lista de números aleatoriamente
print(numeros)
