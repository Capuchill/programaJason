import json 
import os 


data={}
data['estudiantes']=[]

def msgError(msg):
    print (msg)
    input("Presione cualquier tecla para continuar...")

def validarInput(msg):
    while True:
        try:
            n=input(msg)
            if n==None or n.strip()== "":
              msgError("Digite algun dato.")
              continue
            break
        except Exception as e:
            msgError("Ha ocurrido un error ",e)
    return n  


def validarEdad(msg):
    while True:
        try:
            n=int(msg)
            if n<1:
                msgError("La edad debe ser mayor a 0")
                continue
            break
        except ValueError:
            msgError("Recuerde digitar de forma correcta el dato.")
    return n

def validarPeso(msg):
    while True:
        try:
            n=int(msg)
            if n<1:
                msgError("el peso debe ser mayor a 0")
                continue
            break
        except ValueError:
            msgError("Recuerde digitar de forma correcta el dato.")
    return n


def agregarEstudiante():
    os.system('clear')
    print("***REGISTRO***\n")
    nom=validarInput("Nombre: ")
    edad=validarEdad(input("Edad: "))
    peso=validarPeso(input("Peso: "))
    
    data["estudiantes"].append({
        "nombre":nom,
        "edad":edad,
        "peso":peso
    })


seguir=True

while seguir:

    print("\n***OPCIONES***")
    print("\n1. Registrar jugadores")
    print("2. Finalizar")
    op=int(input("\nOpcion -> "))
    if op==1:
        agregarEstudiante()
    if op==2:
        seguir=False



with open ('Jugadores.json','w') as miArchivo:
    json.dump(data,miArchivo,indent=8)