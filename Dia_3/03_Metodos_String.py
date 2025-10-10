texto = "Algo maravilloso sucederá hoy y lo sabes"

mayusculas = texto.upper() # Convierte el texto a mayúsculas
resultado =texto[2].upper() # Convierte el tercer carácter a mayúscula
print(mayusculas)
print(resultado)

minusculas = texto.lower() # Convierte el texto a minúsculas
print(minusculas)

separado = texto.split() # Divide el texto en una lista de palabras
print(separado)

unido = "-".join(separado) # Une la lista de palabras con guiones
print(unido)

encontrado = texto.find("sucederá") # Busca la posición de "sederará" #? si la letra no existe devuelve -1
print(encontrado)

reemplazado = texto.replace("hoy", "mañana") # Reemplaza "hoy" por "mañana"
print(reemplazado)