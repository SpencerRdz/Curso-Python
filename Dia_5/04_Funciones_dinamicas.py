def chequear_tres_cifras(numero):
    return numero  in range(100, 1000)

print(chequear_tres_cifras(456))  # True

def lista_tres_cifras(lista_numeros):
    new_list = []
    for numero in lista_numeros:
        if numero in range(100, 1000):
            new_list.append(numero)
        else:
            pass
    return new_list

print(lista_tres_cifras([50, 7, 89, 23,30])) 

