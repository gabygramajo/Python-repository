# [expresión for elemento in iterable]

# Ejercicio 1: Cuadrados de números
# Dada una lista de números enteros, usá una list comprehension para crear otra lista con el resultado de elevarlos al cuadrado y mostrá el resultado.
numeros = [1, 2, 3, 4, 5]
resultado = [numero**2 for numero in numeros]
print("1) ", resultado)

# Ejercicio 2: Convertir palabras a mayúsculas
# Dada una lista de nombres, creá una nueva lista con todos los nombres en mayúsculas usando list comprehension.
nombres = ["ana", "luis", "carla"]
resultado = [nombre.upper() for nombre in nombres]
print("2) ",resultado)

# Ejercicio 3: Filtrar pares
# A partir de una lista de números enteros, generá otra lista que contenga solo los números pares.
numeros = [10, 13, 17, 20, 24, 29]
resultado = [numero for numero in numeros if numero % 2 == 0]
print("3) ",resultado)

# Ejercicio 4: Filtrar strings por longitud
# Dada una lista de palabras, creá una nueva lista con aquellas que tengan más de 4 letras.
palabras = ["sol", "luz", "mariposa", "flor", "tren", "elefante"]
resultado = [palabra for palabra in palabras if len(palabra) > 4]
print("4) ",resultado)

# Ejercicio 5: Etiquetar como "par" o "impar"
# Dada una lista de números, generá una nueva lista que contenga "par" si el número es par y "impar" si no lo es.
numeros = [1, 2, 3, 4, 5, 6]
# resultado = ["par" for numero in numeros if numero %2 == 0]
resultado = ["par" if numero %2 == 0 else "impar" for numero in numeros]
print("5) ", resultado)

# Ejercicio 6: Reemplazar negativos por 0
# Dada una lista de números que pueden ser positivos o negativos, creá una lista nueva que tenga los mismos valores, pero reemplazando los negativos por 0.
valores = [5, -3, 0, -7, 8, -1]
resultado = [0 if numero < 0 else numero for numero in valores]
print("6) ", resultado)

# Ejercicio 7: Aplanar una lista de listas
# Dada una matriz (lista de listas), generá una lista plana con todos los números usando comprensión anidada.
matriz = [[1, 2], [3, 4], [5, 6]]
resultado = [columna for fila in matriz for columna in fila]
print("7) ", resultado)

# Ejercicio 8: Producto cartesiano
# Dadas dos listas, generá una lista con todos los pares posibles entre los elementos de ambas listas.
colores = ["rojo", "verde"]
talles = ["S", "M", "L"]
# Resultado esperado: [('rojo', 'S'), ('rojo', 'M'), ...]
resultado = [(color, talla) for color in colores for talla in talles]
print("8) ", resultado)

# Ejercicio 9: Crear diccionario de cuadrados
# Dada una lista de enteros, generá un diccionario cuyas claves sean los números y los valores sus cuadrados.
numeros = [1, 2, 3, 4]
resultado = {numero:numero**2 for numero in numeros}
print("9) ", resultado)

# Ejercicio 10: Obtener únicos en mayúscula
# Dada una lista con nombres repetidos, generá un set con los nombres únicos en mayúscula.
nombres = ["ana", "Pedro", "luis", "ANA", "marta","pedro", "luis", "carla", "maRTA"]
resultado = {nombre.upper() for nombre in nombres}
print("10) ", resultado)