#Inicio Juego: Adivina el número aleatorio (Ejercicios de refuerzo)

#Librerias
import random

#Inicialización variables necesarias
intentos = 1
n = random.randint(0,10)

#Introducción de variables correctas
bandera = True
while bandera:

    try:
        num = int(input("Escribe un número entre 1 y 10: "))
        bandera = False

    except:
        print("ES OBLIGATORIO ESCRIBIR UN NÚMERO")
        intentos = intentos + 1

#Número mayor o menor al introducido
while num != n:

    if num == 5:
        print("Por el culo te la hinco, te falta calle")

    if num < n:
        print("El número introducido es menor")
        num = int(input("Introduzca otro número: "))
        intentos = intentos + 1
    else:
        print("El número introducido es mayor")
        num = int(input("Introduzca otro número: "))
        intentos = intentos + 1

#Fin del juego
if n == num:
    print("Felicidades, has ganado el juego")
    print("Ha necesitado un total de", intentos, "intentos")

#Fin del programa