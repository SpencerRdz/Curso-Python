mi_bool = 10 == 25 # False
print(mi_bool)
mi_bool = 5+5 == 10 # True
print(mi_bool)
mi_bool = "100" == 100 # False
print(mi_bool)
mi_bool = 100.0 == 100 # True aunque son de diferente tipo
print(mi_bool)

#comparacion de cadenas
mi_bool = "Hola" == "Hola" # True
print(mi_bool)
mi_bool = "Hola" == "hola" # False
print(mi_bool)
mi_bool = "hola" == "Hola ".lower() # True
print(mi_bool)

#comparacion de desigualdad
mi_bool = 10 != 25 # True