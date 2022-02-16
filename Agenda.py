#Pedir los datos de nombre y telefono

try:
    fdatos = open("agenda.txt", encoding="utf_8")
except:
    fdatos = open("agenda.txt", "w")
    fdatos.close


sn = input("¿Quieres añadir un nuevo contacto? S/N: ")
sn = sn.lower

if sn != "s" or "n":
    print("Valor no reconocido")

if sn == "s":
    fdatos = open("agenda.txt", "a")
    nombre = input("Introduce el nombre de la persona: ")
    numero = int(input("Introduce su número de teléfono: "))

    fdatos.write(nombre, "-", numero)
    fdatos.close
else:
    fdatos.close


