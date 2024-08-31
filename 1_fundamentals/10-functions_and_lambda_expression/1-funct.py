def greet(name):
    print("Hola", name)
    
greet("Eric")
#>> Hola Eric

def add(a = 0, b = 0):
    return a + b

print(f" 1 + 2 = {add(1, 2)}")
print(f" 2 = {add(2)}")
"""
 1 + 2 = 3
 2 = 2
"""