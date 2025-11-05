lista = ["Spencer", "Ana", "Luis", "Marta"]

mis_enumerados = list(enumerate(lista))
print(mis_enumerados)  

for indice in enumerate(lista): # La funcion enumerate devuelve tuplas (indice, valor)
    print(indice)

for indice, nombre in enumerate(lista): # Desempaquetado de tuplas
    print(f"El indice {indice} tiene el nombre {nombre}")