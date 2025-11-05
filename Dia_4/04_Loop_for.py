lista = ["a", "b", "c", "d"]

for letra in lista:
    print(f"letra: {letra}")

for letra in lista: # obtenemos el índice de cada letra
    numero_letra = lista.index(letra) + 1
    print(f"letra: {letra}, numero: {numero_letra}")

lista = ["pablo", "ana", "luis", "marta", "laura", "carlos"]

for nombre in lista: # recorremos la lista y comprobamos si el nombre empieza por 'l'
    if nombre.startswith("l"):
        print(f"Hola {nombre}, tu nombre empieza por 'l'")
    else:
        print("nombre no empieza por 'l'")

numeros = [1, 2, 3, 4, 5, 6,]
suma = 0
for numero in numeros: # sumamos todos los números de la lista
    suma += numero
print(f"La suma total es: {suma}")

for objetos in [[1, 2], [3,4], [5,6]]: # recorremos una lista de listas
    print(objetos)

for numero1,numero2 in [[1, 2], [3,4], [5,6]]: # recorremos una lista de listas y desempaquetamos los valores
    print(numero1)
    print(numero2)

diccionario = {"nombre": "Pablo",
"edad": 30,
"ciudad": "Madrid"}

for clave in diccionario: # recorremos las claves del diccionario
    print(clave)

for item in diccionario.values(): # recorremos los valores del diccionario
    print(item)

for item in diccionario.items(): # recorremos los items (clave, valor) del diccionario
    print(item)

for clave, valor in diccionario.items(): # recorremos los items (clave, valor) del diccionario desempaquetando los valores
    print(f"{clave}: {valor}")