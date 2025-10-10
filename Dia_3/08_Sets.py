my_set = set([1, 2, 3]) 
print(type(my_set))

otro_set = {4, 5, 6}
print(type(otro_set))

print(otro_set)
print(len(otro_set))
print(3 in otro_set) #verifica si el elemento 3 está en el set #! False
print(4 in otro_set) #verifica si el elemento 4 está en el set #! True

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2)) #! {1, 2, 3, 4, 5}

s1.add(4)
print(s1) #! {1, 2, 3, 4}

s1.remove(2)
print(s1) #! {1, 3, 4}

s1.discard(5) # No lanza error si el elemento no existe
print(s1) #! {1, 3, 4}

s1.pop() # Elimina y retorna un elemento aleatorio
print(s1) #! {3, 4}

sorteo = s1.pop() # Elimina y retorna un elemento aleatorio se puede usar para un sorteo
print(sorteo) #! 3

s1.clear() # Limpia el set
print(s1) #! set()