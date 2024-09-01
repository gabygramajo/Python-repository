#Lista de números
numeros = [1,2,3,4,5] 
#Lista de strings
week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] 
#Lista vacía
elementos = [] 
# lista de listas
sublistas = [ [1,2,3], [4,5,6] ] 

# Recorrer listas con for y while
# for
for day in week:
    print(day)
    
# while
i = 0
while i < len(week):
    print(week[i])
    i += 1
    
# Desempaquetado
names = ["Lucas", "Dalma", "Sasha"]
n1, n2, n3 = names
print(n2)