 #AND con and todas las condiciones deben ser True para que el resultado sea True
mi_bool = 4 < 5 and 5 > 6 # False
print(mi_bool)

mi_bool = 55 == 55 and "perro" == "perro" # True
print(mi_bool)

texto = "esta frase es breve"
mi_bool = "frase" in texto and "breve" in texto # True
print(mi_bool)

#OR con or basta con que una condicion sea True para que el resultado sea True

mi_bool = 5 + 5 == 10 or 10 - 5 == 3 # si una condicion es True, el resultado es True
print(mi_bool)

texto = "esta frase es breve"
mi_bool = "frase" in texto or "python" in texto # True
print(mi_bool)
 
#NOT con not invierte el valor de la condicion
mi_bool = not "a" = "a" # False
print(mi_bool)  

mi_bool = not(5 + 5 == 10) # False  
print(mi_bool)