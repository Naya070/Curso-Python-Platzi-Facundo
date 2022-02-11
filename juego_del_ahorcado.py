def read():
    
    with open("./archivos/data.txt", "r", encoding = "utf-8") as f:
        data =[line for line in f]

    print(data)




#def run():
    
    #print("¡Adivina la palabra!")

    #os.system ("cls") #Limpia la consola

if __name__ == '__main__':
    read()

