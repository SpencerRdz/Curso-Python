nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 22]
ciudades = ["Madrid", "Barcelona", "ciudad de Mexico"]

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
    