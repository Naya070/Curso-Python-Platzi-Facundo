#Crear,con un dictionary comprehension, un diccionario cuyas llaves
#sean los primeros 1000 números naturales con sus raíces cuadradas
#como valores.

dict_d = {i:i**0.5 for i in range (1, 1001)}
print(dict_d)