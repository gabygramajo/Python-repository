def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    numero = 0
    if suma > 15:
        numero = max(num1, num2, num3)
    elif suma < 10:
        numero = min(num1, num2, num3)
    else:
        lista = [num1, num2, num3]
        lista.sort()
        numero = lista[1]

    return numero

print(devolver_distintos(5, 2, 9)) #>> 9
print(devolver_distintos(3, 2, 1)) #>> 1
print(devolver_distintos(4, 5, 3)) #>> 4