#Inicio: Imprimir y contar los múltiplos de 3 desde la unidad hasta un número que introducimos por teclado

suma = 0
num = int(input("Introduce el número máximo al que llegaremos: "))

for x in range(1, num, 3):
    suma = suma + x
    print(x)

print("La suma de todos es: ", suma)