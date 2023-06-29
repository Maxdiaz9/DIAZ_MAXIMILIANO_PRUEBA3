
import os
os.system("cls")
import time
from random import randint, shuffle
from funciones import *

print("\tAutomotora AUTOSEGURO te da la bienvenida\t")
time.sleep(3)
os.system("cls")
dueño_certificado = ["Rocio Gomez","Pedro Alboroz","Antonio Neme","Josué Rivas","Maximiliano Diaz"]
nombre_certificado = ["Camión","Moto","Camionetas","Vehículo"]
patente = ["XD8756","CR1359","TH2942","BO1137","MM6482","PZ1465"]
automotora_registros =[]
registro_patente = []
menu = True
while menu == True:
    seleccion = int(input("""
    \t (1) -- GRABAR -- \t
    \t (2) -- BUSCAR -- \t                  
    \t (3) -- IMPRIMIR CERTIFICADOS -- \t                  
    \t (4) -- SALIR -- \t
    \t : """))
    if seleccion == 1:
        automotora_registros.append(grabar())
        os.system("cls")
        print("-- Correcto --")
    elif seleccion == 2:
        patente = input("ingrese la patente del vehiculo:\n")
        encontrado = False
        for registrar in automotora_registros:
            if patente in registrar:
                print(automotora_registros)
                time.sleep(20)
                encontrar = True
                break
        if encontrar is False:
            print("El registro no se ha podido encontrar")
            iterar = True
    elif seleccion == 3:
        print("Imprimiendo el certificado\n")
        time.sleep(1)
        os.system("cls")
        print("*******************\t")
        shuffle(dueño_certificado)
        print("Nombre:")
        print(dueño_certificado[0])
        shuffle(nombre_certificado)
        print("Tipo certificado:")
        print(nombre_certificado[0])
        print("Patente:")
        shuffle(patente)
        print(patente[0])
        print("*******************\t")
        print("Total a pagar:\n")
        print(certificado())
        break                  
    elif seleccion == 4:
        print("Gracias por visitar La automotora “Auto Seguro” | Hasta pronto")
        time.sleep(1)
        os.system("cls")
        break
    else:
        print("Error al ingresar la opcion")
        time.sleep(1)
        os.system("cls")
        iterar = True   
