 #Ejercicio 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado = list(zip(paises,capitales))

for paises,capitales in combinado:
    print(f'La capital de {paises} es {capitales}')

#Ejercicio 2
marcas = ['Adidas','Nike','Puma']
productos =['tenis','ropa','gorras']
mi_zip = (zip(marcas,productos))
print(mi_zip)

#Ejercicio 3
lista_espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
lista_portugues = ["um", "dois", "três", "quatro", "cinco"]
lista_ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(lista_espanol,lista_portugues,lista_ingles))
print(numeros)