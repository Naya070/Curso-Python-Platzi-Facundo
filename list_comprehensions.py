def run():
    
#Imprimir una lista de los números del 1 al 100 al cuadrado
    squares_numbers = []
    for i in range (1,101):
        squares_numbers.append(i**2) 
    print(squares_numbers)    

 #Imprimir una lista de los números del 1 al 100 al cuadrado
 # Sólo si estos no son divisibles entre 3
 # Primera forma de realizarlo   
  #  list_a = []
  #  for numbers in squares_numbers:
  #   if numbers % 3 !=0:
  #    list_a.append(numbers)
  #  print(list_a)
#Segunda forma de realizarlo, con list comprehensions
    list_a = [num**2 for num in range(1,101) if num % 3 != 0]
  
    print(list_a)

if __name__ == '__main__':
    run()