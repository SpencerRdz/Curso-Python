palabra = "Python"
lista_letras = []

for letra in palabra:

    lista_letras.append(letra)

print(lista_letras)

# Usando comprensión de listas
lista_letras  = [letra for letra in palabra] 
print(lista_letras)

numeros = [numero for numero in range(1, 11)] # Genera una lista de números del 1 al 10
print(numeros)

cuadrados = [numero**2 for numero in range(1, 11)] # Genera una lista de los cuadrados de los números del 1 al 10
print(cuadrados)

pares = [numero for numero in range(1, 21) if numero % 2 == 0] # Genera una lista de números pares del 1 al 20
print(pares)

pies = [12, 15, 20, 25, 30]
metros = [pie * 0.3048 for pie in pies] # Convierte una lista de medidas en pies a metros
print(metros)