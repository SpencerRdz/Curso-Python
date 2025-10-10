mi_texto = "Hoy es un buen día para aprender Python"

resultado = mi_texto[0]# Imprime la letra en la posición 0
print(resultado)
resultado = mi_texto[-3] # Imprime la letra en la posición -3 contando desde el final al inicio
print(resultado)
resultado = mi_texto.index("a") # Imprime la posición donde inicia la letra "a" imprime la posicion del la primera "a" que encuentra
print(resultado)
resultado = mi_texto.index("Python") # Imprime la posición donde inicia la palabra "Python"
print(resultado)
resultado = mi_texto.index("a", 10) # Imprime la posición donde inicia la letra "a" pero buscando desde la posición 10
print(resultado)

