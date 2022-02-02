#Listas

vEdades = [1,2,3,4] #La primera posición del rango de la lista es el 0. En este caso, las posiciones van del 0 - 3.
vEdades[0] = 10

for edad in range(0, len(vEdades), 2):
    print(vEdades[edad])


#vEdades.sort() -> Ordena la lista de menor a mayor
#vEdades.pop() -> Elimina el elemento de la posición elegida o, en su defecto, del úlitmo valor
#vEdades.remove -> Igualu