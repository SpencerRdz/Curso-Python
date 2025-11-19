"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""
def cero_repetido(*args):
    for n in range(len(args)-1):
        if args[n] == 0 and args[n+1] == 0:
            return True
    return False

print(cero_repetido(0,6,2,0,1,0,3,2,0))