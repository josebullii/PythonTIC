#Número mayor entre 3 números

#Inicio

print("Número mayor introducido: ")

#Introducir variables

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))

#Comparación

if a>b and a>c:
        print("El mayor es: ", a)
if b>a and b>c:
        print("El mayor es: ", b)
if c>a and c>b:
        print("El mayor es: ", c)