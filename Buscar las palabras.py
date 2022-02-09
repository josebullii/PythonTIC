#Buscar las palabras de un texto

texto = ""
palabra = ""


texto = input("Escribe el texto: ")
texto = texto.strip()


palabra = input("¿Qué palabra estás buscando?: ")
palabra = palabra.lower()
texto = texto.lower()


print(texto.find(palabra))
aux = texto[texto.find(palabra)+1:]