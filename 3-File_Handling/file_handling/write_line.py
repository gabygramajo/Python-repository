file = open('prueba-escribir.txt', 'w')

frases_programadores = [
    "Siempre codifica como si la persona que eventualmente mantendrá tu código fuera un psicópata violento que sabe dónde vives.",
    "No te preocupes si no funciona bien. Si todo lo hiciera, te quedarías sin trabajo.",
    "Cualquier código lo suficientemente avanzado es indistinguible de la magia.",
    "Primero, resuelve el problema. Luego, escribe el código.",
    "La depuración es dos veces más difícil que escribir el código en primer lugar. Por lo tanto, si escribes el código lo más inteligentemente posible, por definición, no eres lo suficientemente inteligente como para depurarlo."
]

for frase in frases_programadores:
    file.write(f'{frase}\n')

file.close()