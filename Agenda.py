#Menú del programa principal
def mostrarMenu():

    seleccion = 0

    while (seleccion<1) or (seleccion>6):
        print("1 - Añadir contacto")
        print("2 - Editar contacto")
        print("3 - Borrar contacto")
        print("4 - Buscar contacto")
        print("5 - Mostrar todos los contactos")
        print("6 - Salir")
        print("")

        try:
            seleccion = int(input("Selecciona una opción: "))
        except:
            seleccion = 0
            print("No es correcto")

        if (seleccion<1) or (seleccion>6):
            print("")
            print("Las opciones son 1, 2, 3, 4, 5 y 6")
            print("")

    return seleccion

mostrarMenu()


