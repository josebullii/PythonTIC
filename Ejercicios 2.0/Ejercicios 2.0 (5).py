#Inicio: Solo se puede introducir S o N


letra = input("Escribe una letra: ")

if ((letra == "N" or "n") or (letra == "S" or "s")):
    print("Esa letra es correcta :)")
else:
    print("Esa letra no es correcta")
    letra = input("Introduce otra letra: ")
    
    