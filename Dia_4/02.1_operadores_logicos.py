 #Ejercicio 1
"""
Verifica si num1 es mayor que num2, y menor que num3. 
Almacena el resultado de dicha comparación en una variable llamada mi_bool.
"""
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num3 and num1 < num3

#Ejercicio 2
"""
Verifica si num1 es mayor que num2, o menor que num3.
 Almacena el resultado de dicha comparación en una variable llamada mi_bool."""
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3

#Ejercicio 3
"""Verifica si las palabras almacenadas en las siguientes variables:
no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:"""

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = (not palabra1 in frase) and (not palabra2 in frase)