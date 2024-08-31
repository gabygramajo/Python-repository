"""
Los iteradores tienen la ventaja de ocupar menos memoria y de ser procesados con mayor velocidad que una estructura de datos tradicional ya que sus elementos son creados al momento de usarlos y no desde antes como las listas. Para construir un iterador sin pasar por otra estructura, es necesario el uso de clases. Por otro lado Un generador se puede interpretar como sugar syntax de los iteradores.
"""

# Iterator
list = [5,1,6,8,2]
print(f"list -> {list}")

iterator = iter(list)

print(f" 1 -> {next(iterator)}")
print(f" 2 -> {next(iterator)}")
print(f" 3 -> {next(iterator)}")
print(f" 4 -> {next(iterator)}")
print(f" 5 -> {next(iterator)}")
"""
list -> [5, 1, 6, 8, 2]
 1 -> 5
 2 -> 1
 3 -> 6
 4 -> 8
 5 -> 2
"""

text = "Python"
print(f"text -> {text}")

iterator = iter(text)

print(f" 1 -> {next(iterator)}")
print(f" 2 -> {next(iterator)}")
print(f" 3 -> {next(iterator)}")
print(f" 4 -> {next(iterator)}")
print(f" 5 -> {next(iterator)}")
"""
text -> Python
 1 -> P
 2 -> y
 3 -> t
 4 -> h
 5 -> o
"""