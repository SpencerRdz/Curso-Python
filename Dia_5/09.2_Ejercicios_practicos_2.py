"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d'
,
'e'
,
'i'
,
'n'
,
'o'
,
'r'
,
't']
"""

def cualquier_nombrer(nombre):
    lista = []
    for letra in nombre:
        lista.append(letra)
    sin_duplicados = set(lista)
    lista = list(sin_duplicados)
    lista.sort()
    return lista
    
print(cualquier_nombrer("hollaaa"))

