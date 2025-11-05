#Ejercicio 1
#Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.

numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

##Ejercicio 2
numero = 50
while numero > -1:
    if numero %5 == 0:
        print(numero)
    numero -= 1

#Ejercicio 3
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero == -1:
        break
    print(numero)