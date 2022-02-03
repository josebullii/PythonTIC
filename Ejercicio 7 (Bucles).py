#Imprimir números del 1 al 100 / Calcular la suma de los pares / Calcular la suma de los impares

i = 0
sumapares = 0
sumaimpares = 0

for i in range (0, 101):
    print(i)

    if  i%2 == 0:
        sumapares = sumapares + i
    else:
        sumaimpares = sumaimpares + i

print("La suma de los números pares es: ", sumapares)
print("La suma de los números impares es: ", sumaimpares)

