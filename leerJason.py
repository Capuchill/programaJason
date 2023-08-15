import json
datosDian={}
datosDian['Clientes']=[]
with open ('Ahorradores.json') as usuarios:
    data=json.load(usuarios)
    for elem in data['cliente']:
        cont=0
        if elem['Saldo']> 35000000:
            cont+=1
            print(f"Cliente #{cont}: \n")
            print(f"Numero de cuenta: {elem['NumCuenta']}")
            print(f"Numero de cuenta: {elem['Saldo']}")

            cliente={}
            cliente['consecutivo']=cont
            cliente['NumCuenta']= elem['NumCuenta']
            cliente['Saldo']= elem['Saldo']
            datosDian['Clientes'].append(cliente)
with open ('Dian.json','w') as miArchivo:
    json.dump(datosDian,miArchivo,indent=8)
