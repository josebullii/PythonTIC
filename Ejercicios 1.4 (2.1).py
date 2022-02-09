#Ejercicio 2 en una función

def imprimeConMayusculas(palabra):
    
    palabra = palabra.lower()

    bandera = True

    for i in palabra:
        if bandera == True:
            print(i.upper(), end="")
        else:
            print(i, end="")

        bandera = not(bandera)
    return bandera

palabra = input("Escribe una palabra: ")
imprimeConMayusculas(palabra)