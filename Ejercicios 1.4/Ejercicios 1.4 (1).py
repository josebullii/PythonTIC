#Escribir las palabras introducidas al reves (Jose -> esoJ)

palabra = input("Introduce una palabra: ")
tam = len(palabra) - 1

while tam>=0:
    print(palabra[tam], end="")
    tam = tam - 1