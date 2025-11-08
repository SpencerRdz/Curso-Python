 #?Ejercicio 1
# Declara una función llamada todos_positivos que reciba una lista de números como parámetro 
# y retorne True si todos los números en la lista son positivos, o False si al menos uno de ellos es negativo.
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
            
        else:
            pass
    return True
lista_numeros = [5,-4,3]

#? Ejercicio 2
# declara una función llamada suma_menores que reciba una lista de números como parámetro
# y retorne la suma de todos los números menores a 1000 en la lista.
def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(0,1000):
            suma += numero
        else: 
            pass
    return suma
lista_numeros = [5,5,10000]

#? Ejercicio 3
# Declara una función llamada cantidad_pares que reciba una lista de números como parámetro
# y retorne la cantidad de números pares en la lista.
def cantidad_pares(lista_numeros):

    pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            pass
    
    return pares
lista_numeros = [4,7,2,8,9,4]
resultado = cantidad_pares(lista_numeros)
print(resultado)