#Número de palabras de un/a frase/texto

contador = 1

texto = input("Escribe una frase: ")
tam = len(texto) + 1

for i in texto:
    if i == (" ") and texto(i + 1) != (" "):
        contador = contador + 1

print("Esta frase tiene", contador, "palabras")
