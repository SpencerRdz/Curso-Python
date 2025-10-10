verdadero = True
falso = False
print(type(verdadero)) #! <class 'bool'>
print(type(falso)) #! <class 'bool'>

#Mayor que
numero = 5 > 2+3
print(numero) #! False

#Igual que
numero = 5 == 2+3
print(numero) #! True

#Distinto que
numero = 5 != 2+3
print(numero) #! False

#Mayor o igual que
numero = 5 >= 2+3
print(numero) #! True

#Encontrar un elemento en una lista
lista = [1, 2, 3]
print(3 in lista) #! True