 #? Ejercicio 1: Convertir una cadena a mayúsculas
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
mayuscula = frase.upper()
print(mayuscula)

#? Ejerciccio 2: unir una lista de palabras en una sola cadena
lista_palabras = ["La","legibilidad","cuenta."]
unir = ' '.join(lista_palabras)
print(unir)

#? Ejercicio 3: Reemplazar palabras en una cadena
texto = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
remplazar = texto.replace('difícil','fácil')
remplazar2 = remplazar.replace('mala','buena')
print(remplazar2)