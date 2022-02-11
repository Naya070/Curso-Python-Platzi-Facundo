#Crear un diccionario cuyas llaves sean los cien
#primeros números naturales y cuyos valores sean
#esos mismos números elevados al cubo.
dict_a = {}
for i in range (1, 101):
    dict_a[i] = i**3
    
#print(dict_a)

#Crear un diccionario cuyas llaves sean los cien
#primeros números naturales y cuyos valores sean
#esos mismos números elevados al cubo. Guardar en las llaves sólo
#los números que no sean divisibles por 3.
dict_b = {}
for i in range (1, 101):
   if i % 3 !=0:
        dict_b[i] = i**3
    
#print(dict_b)

#Realizamos el código anterior pero con dict comprehensions

dict_c = {i:i**3 for i in range(1, 101) if i % 3 != 0}

print(dict_c)