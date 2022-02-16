#Inicio

total = 0
contador = 0
mayor = 0
menor = 0
media = 0

n = int(input("Introduce números reales (Con 0 cierras el programa): "))

while n!=0:
    total = total + n
    contador = contador + 1

    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

if n == 0:
    media = total / contador

    print("La media total es: ", media)
    print("El número mayor es: ", mayor)
    print("El número menor es: ", menor)