nombre =  input("¿Cuál es tu nombre? ")
ventas_enero = float(input("¿Cuánto vendiste en enero? "))
comision = round(ventas_enero * 0.13, 2)

print(f"Hola {nombre}, la comision por tus ventas es de ${comision}. ¡Buen trabajo!")