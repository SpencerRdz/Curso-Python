def desempaquetar_suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        total += valor
    return total

print("Suma de valores:", desempaquetar_suma(a=5, b=10, c=15))


def imprimir_info(num1,num2,*args,**kwargs):
    print("Número 1:", num1)
    print("Número 2:", num2)

    for arg in args:
        print("Argumento adicional:", arg)

    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_info(1, 2, "extra1", "extra2", nombre="Juan", edad=30)


def desempaquetar_argumentos(*args, **kwargs):
    for arg in args:
        print("Argumento:", arg)    

    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

args = ["valor1", "valor2", "valor3"]
kwargs = {"clave1": "valorA", "clave2": "valorB"}
desempaquetar_argumentos(*args,**kwargs)