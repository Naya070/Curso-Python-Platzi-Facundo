#Crear una list comprehension para crear una lista de números del
# 1 al 5 pero elvados al cuadrado.

list_com = [i**2 for i in range (1,6)]
#print(list_com)

#también:

list_a = [1,2,3,4,5]

list_b = [i**2 for i in list_a]

print(list_b)