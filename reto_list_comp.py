#Crear una list comprehensions para realizar una lista de todos los
#múltiplos de 4 que a la vez también son múltiplos de 6 y de 9,
#hasta 5 dígitos

list_b = [i for i in range(1,1000000) if i % 4 == 0 if i % 6 == 0 if i % 9 == 0 if len(str(i))<=5]


print(list_b)