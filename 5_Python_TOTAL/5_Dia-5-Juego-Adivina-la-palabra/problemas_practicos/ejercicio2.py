def devolver_caracteres_unicos(palabra):
    caracteres = list(set(list(palabra)))
    caracteres.sort()
    return caracteres

print(devolver_caracteres_unicos("entretenido"))