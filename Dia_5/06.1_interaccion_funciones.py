#?Ejercicio 1
# Simula el lanzamiento de dos dados y evalúa la jugada según la suma obtenida.
from random import randint

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    
    return dado1, dado2

def evaluar_jugada(primer_dado,segundo_dado):
    suma_dados = primer_dado + segundo_dado
    
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
        
primer_dado,segundo_dado = lanzar_dados()
jugada = evaluar_jugada(primer_dado,segundo_dado)


#?Ejercicio 2
# reduce una lista de números eliminando duplicados, ordenándola y quitando el mayor valor. 
# Luego calcula el promedio de los números restantes.
lista_numeros = [1,2,15,7,2,8]
 
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
 
def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio

lista_reducida = reducir_lista(lista_numeros)
promedio_listaa = promedio(lista_reducida)

#?Ejercicio 3
# simula el lanzamiento de una moneda para decidir si se destruye o se salva una lista de números.
from random import choice

lista_numeros = [1,2,15,7,2,8]
def lanzar_moneda():
    resultado = choice(["Cara", "Cruz"])
    return resultado
 
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista
