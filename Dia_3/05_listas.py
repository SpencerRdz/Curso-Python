mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]

print(type(mi_lista))  #? imprime <class 'list'>
print(len(mi_lista))   #? imprime 3
resultado = mi_lista[0]  #? accede al primer elemento
print(resultado)  #? imprime 'a'
print(mi_lista+mi_lista2)  #? concatena dos listas

otra_lista = ["Hola", 123, 45.67, True, [1, 2, 3]]

mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = "A"  #? las listas son mutables, se puede modificar directamente
print(mi_lista3)  

mi_lista3.append("g")  #? agrega un elemento al final de la lista
print(mi_lista3)

mi_lista3.pop()  #? elimina el último elemento de la lista
print(mi_lista3)

eliminado = mi_lista3.pop(2)  #? elimina el elemento en la posición 2
print(eliminado)  #? imprime el elemento eliminado

lista = ["f", "e", "d", "c", "b", "a"]
lista.sort()  #? ordena la lista
print(lista)  #? imprime ['a', 'b', 'c', 'd', 'e', 'f']

lista.reverse()  #? invierte el orden de la lista
print(lista)  #? imprime ['f', 'e', 'd', 'c',