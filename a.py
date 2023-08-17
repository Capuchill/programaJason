import json 
#hahahha
data={}
data['clients']=[]

data['clients'].append({

    'firstName':'Theo',
    'lastName':'rivers',
    'age':36,
    'amount':1.11})


data['clients'].append({'firstName':'juan',
    'lastName':'jimenez',
    'age':23,
    'amount':1.20 })

with open ('misdatos.json','w') as file:
    json.dump(data,file,indent=8)