 #?# Estructuras de control: while, else, pass, break, continue
monedas = 5
while monedas > 0:
    print("Tienes", monedas, "monedas.")
    monedas -= 1
else:
    print("Ya no tienes monedas.")

respuesta = "s"
while respuesta == "s":
    respuesta = input("¿Quieres continuar? (s/n): ")
else:
    print("Has decidido no continuar.")

# PASS, BREAK, CONTINUE

while respuesta == "s":
    pass 

print("Este mensaje se imprimirá una sola vez debido al 'pass' en el bucle.")

nombre = "Spencer" 
for letra in nombre: # se itera sobre cada letra en la cadena "Spencer" y si encuentra una "n", se detiene el bucle.
    if letra == "n":
        break
    print(letra)
 
for letra in nombre: # se itera sobre cada letra en la cadena "Spencer" y si encuentra una "n", se salta esa iteración.
    if letra == "n":
        continue
    print(letra)