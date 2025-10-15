if  10 > 9:
    print("Es correcto")


if 10 < 9:
    print("Es correcto")
else:
    print("No es correcto")

mascota = "perro"

if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
elif mascota == "pez":
    print("Tienes un pez")
else:
    print("No se que animal tienes")

edad = 16
calificacion = 8
if edad < 17:
    print("Eres menor de edad")
    if calificacion >= 6:
        print("Estas aprobado")
    else:
        print("Estas reprobado")
else:
    print("Eres mayor de edad")