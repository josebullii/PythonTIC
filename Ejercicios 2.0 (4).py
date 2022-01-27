#Inicio: Suma de los primeros 100 numeros

#1º Manera
suma = 0

for x in range(0,101):
    suma = x + suma
    
print("La suma de los 100 primeros números es: ", suma)


#2º manera

print(sum(range(1, 101)))