#Alternar mayusculas y minusculas

palabra = input("Escribe una palabra: ")
palabra = palabra.lower()

bandera = True

for i in palabra:
    if bandera == True:
        print(i.upper(), end="")
    else:
        print(i, end="")
    
    bandera = not(bandera)
