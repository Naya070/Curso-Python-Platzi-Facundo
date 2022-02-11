#Programa con un error para aprender debugging.

def divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:  #Debería ser : if num % i == 0:
            divisors.append(i)
    return divisors        


def run():
    num = input("Ingresa un número: ")
    assert num > '0' , "Debes ingresar un número positivo"
    assert num.isnumeric(), "Debes ingresar un número"
    
    print(divisors(int(num)))
    print("Terminó mi programa")
    

  

if __name__ == '__main__':
    run()    