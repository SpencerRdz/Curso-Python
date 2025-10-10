 #! Propiedades de los Strings

#Inmutabilidad de los Strings
nombre = "Carina"
#nombre[0] = "K"  #? los strings son inmutables, no se pueden modificar directamente
nombre = "karina"
print(nombre) 

#Concatenación de Strings
n1 = "Kari"
n2 = "na"
nombre = n1 + n2  #? concatenación
print(nombre)

#Repetición de Strings
nombre = "Kari" * 3  #? repetición
print(nombre)

# Saltos de línea en Strings
poema = """Rosas son rojas,
Violetas son azules,  
El pasto es verde,
Y yo te quiero a ti."""
print(poema)
print("Rosas" in poema)  #? verifica si "Rosas" está en el string poema 
print("Rosas" not in poema)  #? verifica si "Rosas" no está en el string poema

# Longitud de un String
print(len(poema))  #? imprime la longitud del string poema

