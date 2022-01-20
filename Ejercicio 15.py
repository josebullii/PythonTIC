#Inicio

#Inicializar variables (no están definidas al solo aparecer en instrucciones)
num = 0
media = 0
contador = 0

print("Introduce todos los números que quieras (con -1 se cierra)")

n = int(input("Introduce el número: "))

while n!=-1:
    num = num + n 
    contador = contador + 1

    n = int(input("Introduce otro número: "))

if n==-1:
    media = num / contador

    print("La media de los números introducidos es: ", media)
