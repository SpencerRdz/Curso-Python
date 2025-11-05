 #? Ejercicio 1
# Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor **2 for valor in valores]

# Ejercicio 2
 # Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [valor for valor in valores if valor % 2 == 0]

# Ejercicio 3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius =[(grados_fahrenheit-32)*(5/9) for grados_fahrenheit in temperatura_fahrenheit]