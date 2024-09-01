import random

#Generar un número entero aleatorio
random_number = random.randint(1, 10)
print(f"El numero aleatorio es: {random_number}")

#Color aleatorio
colors = ["Red", "Blue", "Yellow"]
random_color = random.choice(colors)
print(f"El color aleatorio es: {random_color}")

#Barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
#desordenar lista
random.shuffle(cards)
print(cards)

def f(x): return x * 2 
print("f: ",f(3))

try: 
    1 / 0 
except ZeroDivisionError: 
    print("Error")
