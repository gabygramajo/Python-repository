# Lista de 2 dimensiones
matrixA = [
    [10,20,30],
    [60,70,80],
    [90,100,200]
]
print(f"matrixA = {matrixA}")
print(f"matrixA[1][2] = {matrixA[1][2]}")
"""
matrixA = [[10, 20, 30], [60, 70, 80], [90, 100, 200]]
matrixA[1][2] = 80
"""


# Lista de 3 dimensiones
matrixB = [
    [10,[100,1000]],
    [20,[200, 2000]],
    [30,[300, 3000]]
]
print(f"matrixB {matrixB}")
print(f"matrixB[1][1] = {matrixB[1][1]}")
print(f"matrixB[1][1][0] = {matrixB[1][1][0]}")
"""
matrixB [[10, [100, 1000]], [20, [200, 2000]], [30, [300, 3000]]]
matrixB[1][1] = [200, 2000]
matrixB[1][1][0] = 200
"""