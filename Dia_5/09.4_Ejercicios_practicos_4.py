def contar_primos(numero):
    lista_primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    
    while iteracion <= numero:
        es_primo = True
        for primo in lista_primos:
            if iteracion % primo == 0:
                es_primo = False
                break
        if es_primo:
            lista_primos.append(iteracion)
        iteracion += 2
    return f"Los numeros primos son: {lista_primos} cantidad de primos:{len(lista_primos)}"

print(contar_primos(50))