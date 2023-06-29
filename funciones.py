import os
os.system("cls")
import time
from random import randint, shuffle

def grabar():
    registrar = []
    while True:
        tipo  = input("Ingresa el tipo de vehículo (ref: MOTO - CAMIÓN... ETC):\n")
        if len(tipo) >=2 and len(tipo)<= 20:
            registrar.append(tipo)
            break
    while True:
        marca = input("Ingresa la marca del vehículo:\n ")
        if len(marca) >=2 and len(marca) <=15:
            registrar.append(marca)
            break
        else:
            print("Error: La marca debe contener entre 2 y 15 caracteres como máximo")
    while True:
        patente = input("Ingresa la patente del vehículo:\n")
        if len(patente) >=5 and len(patente) <= 6:
            registrar.append(patente)
            break
        else:
            print("Error: La patente debe tener 6 caracteres (Ej: XH7489)")
            break
    while True:
        precio = int(input("Ingresa el precio del vehículo:\n"))
        if precio > 4999999:
            registrar.append(precio)
            break
        else:
            print("Error: El precio debe ser mayor a $5.000.000")
            
    while True:
        time.sleep(3)
        nombre_dueño = input("Ingresar nombre del dueño del vehículo :\n")
        if len(nombre_dueño.lower()) >=1:
            registrar.append(nombre_dueño)
        else:
            print("Error: El nombre del dueño debe contener solo letras")
            break
    while True:
        print("La fecha debe tener el formato DD-MM-YYYY")
        fecha_registro = input("Ingresa la fecha del registro:\n")
        if len(fecha_registro) >7 and (fecha_registro) <11:
            registrar.append(fecha_registro.replace("-",""))
        else:
            print("Error: Recuerda día-mes-año ")
            break
    while True:
        multa = input("Vehículo con multas? -- SI o 'NO --\n")
        if multa.lower() in ["si","no"]:
            registrar.append(multa)
            break
        else:
            print("Opcion invalida por favor indique con: SI o NO\n")
            
    while True:
        fecha_multa = input("Si tiene multas indique la fecha (dd/mm/yy) de lo contrario indique (NO):\n")
        if len(fecha_multa) >= 2 and len(fecha_multa) <= 15:
            registrar.append(fecha_multa)
            break
        else:
            print("Opcion invalida, indique la fecha (dd/mm/yy) o la opción 'NO' \n")
    return registrar


def buscar_patente(patente, automotora_registros):
    patente = input("ingrese la patente del vehiculo:\n")
    encontrado = False
    for registrar in automotora_registros:
        if patente in automotora_registros:
            print(registrar)
            encontrado = True
            break
    if encontrado is False:
        print("Registro no encontrado.")
        
def certificado():
        valor = randint(1500,3500)
        return valor

def salir():
    print("Gracias por visitarnos Automotora *Auto Seguro* ")
    time.sleep(3)
    os.system("cls")
