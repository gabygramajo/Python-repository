"""
Para realizar operaciones sencillas con lambda, no necesitamos especificar el nombre de la función. Solo requerimos parámetros y la operación deseada. Por ejemplo, para sumar dos números, podemos definir una función lambda así:
"""
add = lambda a,b: a+b
print(f"add(4, 9) -> {add(4, 9)}")
#>> add(4, 9) -> 13

# map -> https://www.w3schools.com/python/ref_func_map.asp
square = lambda x: x**2
numbers = range(11)
squared_numbers = list(map(square, numbers))
print("Cuadrados:", squared_numbers)
#>> Cuadrados: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter -> https://www.w3schools.com/python/ref_func_filter.asp
even_numbers = lambda x: x%2 == 0
numbers = range(21)
even_numbers_list = list(filter(even_numbers, numbers))
print(f"even numbers from 0 to 20 -> {even_numbers_list}")