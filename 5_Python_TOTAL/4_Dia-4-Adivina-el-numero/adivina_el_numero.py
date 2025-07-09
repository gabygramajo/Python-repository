from random import randint
magic_number = randint(1, 100)
attempts = 0
player_number = 0

print("### ADIVINA EL NÚMERO MÁGICO ###")
user_name = input("Introduce tu nombre: ")
print(f"Hola {user_name}, he pensado un número mágico entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

while attempts < 8:
    player_number = int(input(f"Ingresar número ({attempts + 1}/8):"))

    if player_number not in range(1, 101):
        print("has elegido un número que no está permitido. Vuelve a intentarlo.")
        continue

    if player_number == magic_number:
        print(f"¡¡¡Felicidades, has adivinado el número mágico \"{magic_number}\" en {attempts + 1} intentos!!!")
        break
    elif player_number < magic_number:
        print("El número elegido es menor al número mágico")
    elif player_number > magic_number:
        print("El número elegido es mayor al número mágico")

    attempts += 1

if magic_number != player_number :
    print(f"Se acabaron los intentos. El número magico era \"{magic_number}\"")