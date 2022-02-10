#Decir cuantas vocales tiene un nombre

contador = 0
palabra = input("Escribe una palabra: ")
tam = len(palabra)

for i in palabra:
    if i == "a" or i == "e"  or i == "i" or i == "o" or i == "u":
        contador = contador + 1

print("Hay un total de ", contador, "vocales")