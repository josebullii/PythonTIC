nombre = input("Escribe tu nombre: ")
nombre = nombre.lower()

bandera = False

for i in nombre:
    if i == " ":
        bandera = True
        if bandera == True:
            
