# El Slice en la listas permite solo copiar la información y no apuntar o hacer referencia a la dirección de memoria de la lista, evitando asi la mutabilidad.

# Sin Slice
a = [1,2,3,4,5]
b = a
print(f"a: {a}")
print(f"b: {b}")

del a[0]

print(f"a: {a}")
print(f"b: {b}")
"""
a: [1, 2, 3, 4, 5]
b: [1, 2, 3, 4, 5]
a: [2, 3, 4, 5]
b: [2, 3, 4, 5]
"""

print(f"a -> {id(a)} b -> {id(b)}. a == b -> {id(a) == id(b)}")
# a -> 140095939693376 
# b -> 140095939693376

# Con Slicing
c = a[:]
print(f"a -> {id(a)} b -> {id(c)}. a == c -> {id(a) == id(c)}")

a.append(6)
print("a", a)
print("c", c)