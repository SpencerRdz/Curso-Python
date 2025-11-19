 #?Ejercicio 1
# Funcion que recibe una cantidad variable de argumentos y devuelve la suma de sus cuadrados.
def suma_cuadrados(*args):
    total = 0
    for num in args:
        total += num*2
    return total
    
resultado = suma_cuadrados(1,2,3)
print(resultado)

    #?Ejercicio 2
# Funcion que recibe una cantidad variable de argumentos y devuelve la suma de sus valores absolutos.
def suma_absolutos(*args):
    total = 0 
    for num in args:
        total += abs(num)
    return total
    
#?Ejercicio 3
# Funcion que recibe un nombre y una cantidad variable de números, y devuelve un mensaje con la suma de esos números.
def numeros_persona(nombre,*args):
    nombre = nombre
    suma_numeros = 0 
    for n in args:
       suma_numeros += n
    return f"{nombre}, la suma de tus números es {suma_numeros}"

