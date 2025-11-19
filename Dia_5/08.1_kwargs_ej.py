 #? Ejercicio 1
#contar la cantidad de atributos pasados como keywords arguments
def cantidad_atributos(**kwargs):
    lista = []
    for clave in kwargs.items():
        lista.append(clave)
    return len(lista)

#? Ejercicio 2
#crear una lista con los valores de los atributos pasados como keywords arguments
def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(valor)
    return lista
print(lista_atributos(nombre="Ana", edad=25, ciudad="Madrid"))  

#? Ejercicio 3
#crear una función que reciba un nombre y varios atributos adicionales como keywords arguments e imprima una descripción de la persona
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')



