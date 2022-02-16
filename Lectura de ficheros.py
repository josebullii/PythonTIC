
''' Lectura de ficheros de texto

from encodings import utf_8


fdatos = open("datos.txt", encoding="utf_8", "r")

for linea in fdatos:
    print(linea)

fdatos.close()

'''


fdatos = open("nombres.txt", "a")

fdatos.write("Jose\nSiuu")

fdatos.close()