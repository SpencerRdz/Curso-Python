texto = "El amor es el sentimiento mas puro que existe en el mundo, el amor es lo que mueve al mundo" #input("Ingrese un texto: ")
texo_minusculas = texto.lower()

letra = input("Ingrese una letra: ")
letra_2 = input("Ingrese otra letra: ")
letra_3 = input("Ingrese otra letra: ")


letras = []
letras.append(letra.lower())
letras.append(letra_2.lower())
letras.append(letra_3.lower())

# NUMERO 1: CONTADOR DE LETRAS EN UN TEXTO
x,y,z = letras
print(texo_minusculas)
print(f"La letra '{x}', aparece {texo_minusculas.count(x)} veces en el texto")
print(f"La letra '{y}', aparece {texo_minusculas.count(y)} veces en el texto")
print(f"La letra '{z}', aparece {texo_minusculas.count(y)} veces en el texto")

# NUMERO 2:CONTADOR DE PALABRAS EN UN TEXTO
lista_palabras = texto.split()
numero_palabras = len(lista_palabras)
print(f"El texto tiene {numero_palabras} palabras")

# NUMERO 3: PRIMERA LETRA DEL TEXTO
print(f"La primera letra del texto es: {texto[0:1]}")

# NUMERO 4: INVERSOR DE TEXTO
print(f"""
Asi se ve el texto al reves:
      
{texto[::-1]}

""") 

# NUMERO 5: BUSCADOR DE PALABRAS
print(f" la palabra Python se encuentra en el texto: {'python' in texo_minusculas}")