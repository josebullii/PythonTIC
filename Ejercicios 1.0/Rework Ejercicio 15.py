#Ejercicio 15, pero con listas

vNum = []
num = 0
media = 0

num = int(input("Escribe un número (con -1 se cierra el programa): \n"))

while num != -1:
    num = int(input("Escribe otro número: \n"))

    if num != -1:
        vNum.append(num)

if num == -1:

    vNum.sort()
    print("Los números leídos por son: ", len(vNum), "y son: ", vNum)

    print("El mayor es: ", max(vNum))

    print("El menor es: ", min(vNum))

    media = sum(vNum)/len(vNum)
    print("La media de los números introducidos es: ", media)
