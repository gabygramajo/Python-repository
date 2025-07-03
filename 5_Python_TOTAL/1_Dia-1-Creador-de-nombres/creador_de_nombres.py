print("### BIENVENIDO AL CREADOR DE NOMBRES ###")

word_1 = input("¿Cuál es el nombre de tu mascota favorita? ").lower()
word_2 = input("¿Cuál es tu color favorito? ").lower()

name = (word_1 + " " + word_2).capitalize()

print(f"Generando nombre... \n El nombre para tu emprendimiento será:\n\n \"Cervecería {name}\"")