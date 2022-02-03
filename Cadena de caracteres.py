nombre = "Jose va a casa de su tocayo, que también se llama Jose"
cont = 0

nombre = nombre.strip() #Elimina los espacios vacíos
tam = len(nombre)

#print(nombre)

for i in nombre:    #Recorre la cadena
    if i == "o":
        cont+=1

#print(cont)

nombre = nombre.lower() #Pasar a minúscula
#nombre = nombre.upper() #Pasar a mayúscula

print(nombre.find("jose"))
aux = nombre[nombre.find("jose")+1:]
print(aux.find("jose"))