def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = suma(1, 2, 3, 4, 5)
print("La suma es:", resultado)
