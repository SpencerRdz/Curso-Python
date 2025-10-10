mi_tuple = (1, 2, 3, 4, 5)
print(type(mi_tuple))
print(mi_tuple[0])

mi_new_tuple = (1,4,(5,6),7)
print(mi_new_tuple[2][1])

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

t = (1,2,3,1)
x,y,z,a = t
print(x,y,z)
print(len(t))
print(t.count(1))
print(t.index(3))