from random import *
numero_magico = randint(1, 100)
intentos = 0
number = 0

print("### ADIVINA EL NÚMERO MÁGICO ###")
user_name = input("Introduce tú nombre: ")
print(f"Hola {user_name}, he pensado un número mágico entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

while intentos < 8:
    number = int(input(f"Ingresar número ({intentos + 1}/8):"))

    if number not in range(1, 100):
        print("haz elegido un número que no está permitido. Vuele a intentarlo.")
        continue

    if number == numero_magico:
        print(f"¡¡¡Felicidades, haz adivinado el número mágico \"{numero_magico}\" en {intentos + 1} intentos!!!")
        break
    elif number < numero_magico:
        print("El número elegido es menor al número mágico")
    elif number > numero_magico:
        print("El número elegido es mayor al número mágico")

    intentos += 1

if numero_magico != number : print(f"Se acabaron los intentos. El número magico era \"{numero_magico}\"")