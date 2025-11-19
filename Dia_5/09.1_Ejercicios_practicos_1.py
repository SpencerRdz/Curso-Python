"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""
def devolver_disitintos(num1,num2,num3):
    lista = [num1,num2,num3]
    for num in lista:
        if sum(lista) > 15:
            return max(lista)
        elif sum(lista) < 10:
            return min(lista)
        elif sum(lista) > 15 and sum(lista) < 10:
            lista.remove(max(lista))
            lista.remove(min(lista))
        return num
            

print(devolver_disitintos(5,7,1))
        
