diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(type(diccionario))

resultado = diccionario["clave1"] # Acceder al valor asociado a "clave1"
print(resultado)

cliente = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30,
    "altura": 1.75,}

consulta = cliente["apellido"]  # Acceder al valor asociado a "apellido"
print(consulta)

clientes = {
    "cliente1": {
        "nombre": "Ana",
        "edad": 28
    }, 
    "cliente2": {
        "nombre": "Luis",
        "edad": 34
    }
}# Diccionario anidado con mas diccionarios 

print(clientes["cliente1"]["nombre"])  # Acceder al nombre del cliente1 
clientes["cliente1"]["peso"] = 59  # Modificar la edad del cliente1
print(clientes)
clientes["cliente3"] = {"nombre": "Marta", "edad": 25}  # Agregar un nuevo cliente
print(clientes)

dic = {"c1":["a", "b", "c"], "c2":["d", "e", "f"]}
print(dic["c2"][1].upper())  # Acceder a la segunda letra de la lista asociada a "c2" y convertirla a mayúscula

print(dic.keys())  # Obtener todas las claves del diccionario
print(dic.values())  # Obtener todos los valores del diccionario
print(dic.items())  # Obtener todas las claves y valores del diccionario