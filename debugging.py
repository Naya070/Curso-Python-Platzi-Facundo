#Programa con un error para aprender debugging.

def divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 1:  #Debería ser : if num % i == 0:
            divisors.append(i)
    return divisors        


def run():
   try:
    num = int(input("Ingresa un número: "))
    print(divisors(num))
    print("Terminó mi programa")
   except ValueError:
     print("Debes ingresar un número")

     
   try:
    num = int(input("Ingresa un número: "))
        if num < 0:
            raise ValueError
    print(divisors(num))
    print("Terminó mi programa") 

     except ValueError:
         if num < 0:
             print("Debes ingresar un número positivo")
         else:
             print("Debes ingresar un número positivo")

     
  

if __name__ == '__main__':
    run()    