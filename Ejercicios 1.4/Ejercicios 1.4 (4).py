#Vocales de una palabra en orden y sin repetir

palabra = input("Escribe una palabra: ")
palabra = palabra.lower()

vocales = ("a", "e", "i", "o", "u")

for i in vocales:

    for j in palabra:
        if i == j:
            print(i, end="")
            break
