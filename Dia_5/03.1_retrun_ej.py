#Ejercico 1
# Declara una función llamada potencia que reciba dos parámetros numero1 y numero2, y retorne la potencia de entre ambos números.
def potencia(numero1,numero2):
    total = numero1 ** numero2
    return total
print(potencia(3,4))
     

#Ejercicio 2
# Declara una función llamada usd_a_eur que reciba un parámetro dolares y retorne su conversión a euros (1 dólar = 0.9 euros).
def usd_a_eur(dolares):
    euros = dolares * 0.9
    return euros
dolares = usd_a_eur(10)
print(dolares)
    
#Ejercicio 3
# Declara una función llamada invertir_palabra que reciba un parámetro palabra, y retorne la palabra invertida y en mayúsculas.
def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1].upper()
    return palabra_invertida

palabra = invertir_palabra('Python')
print(palabra)
