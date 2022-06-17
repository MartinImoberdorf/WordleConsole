import csv
import os
import random
import sys

def buscarPalabra():
    data=[]

    with open('bbdd.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                data.append(row['Paises'])

    palabra=random.choice(data)
    return palabra

def main():
    #BUSCAR PALABRA
    palabra=buscarPalabra()


    #TITULO
    print("-"*60)
    print(chr(27)+"[1;33m" + "W",chr(27)+"[1;32m" + "O",chr(27)+"[1;34m" + "R",chr(27)+"[1;31m" + "D",chr(27)+"[1;35m" + "L",chr(27)+"[0;32m" + "E")
    print("-"*60)
    print(chr(27)+"[1;37m" + "")


    #INFORMACION Y PRIMERA ENTRADA
    print("La palabra a adivinar tiene ",len(palabra),"caracteres.")
    palabraAIngresar=input("Palabra: ").lower()

    total_random=[]
    intentos=1


    def yellow(letra,palabra):
        n=False
        for i in palabra:
            if i ==letra:
                n=True
        return n

    #LOGICA
    while palabraAIngresar!=palabra:
            if intentos==5:
                    break

            while len(palabraAIngresar)!=len(palabra) or palabraAIngresar.isnumeric():
                    print(chr(27)+"[1;31m" + "Error superó el máximo de caracteres...")
                    print(chr(27)+"[1;37m" + "")
                    palabraAIngresar=input("Palabra: ").lower()

            for x in palabra:
                    total_random+=x
            c=0
            for y in palabraAIngresar:
                if y == total_random[c]:
                    print(chr(27)+"[1;32m" + y)
                    print(chr(27)+"[1;37m" + "")
                else:
                    if  yellow(y,palabra)==True:
                        print(chr(27)+"[1;33m" + y)
                        print(chr(27)+"[1;37m" + "")
                    else:
                        if y != total_random[c]:
                            print(chr(27)+"[1;31m" + y)
                            print(chr(27)+"[1;37m" + "")
                    
                c=c+1
                
            intentos+=1

            print("-"*60)
            palabraAIngresar=input("Palabra: ").lower()
                
            

    if intentos<5:
        #FINAL
        print("-"*60)
        print(chr(27)+"[1;32m" + "Palabra acertada!")
        print(chr(27)+"[1;32m" +"Aceptaste la palabra en",intentos,"intentos.")
        print(chr(27)+"[1;37m" + "")

    else:
        #FINAL
        print("-"*60)
        print(chr(27)+"[1;31m" + "Perdiste!",chr(27)+"[1;37m"+"")
        print(chr(27)+"[1;31m" + "La palabra era: ",chr(27)+"[1;30m" + palabra)
        print(chr(27)+"[1;37m" + "")


    out=int(input("Escriba 1 para volver a jugar..."))
    if out==1:
        os.system("cls")
        main()
    else:
        print("Adios...")
        sys.exit()


if __name__ == '__main__':
    main()