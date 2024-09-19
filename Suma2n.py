def suma_pares(matriz):
    suma_pares = 0
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] % 2 == 0:
                suma_pares += matriz[i][j]
    return suma_pares

# Ejemplo:
matriz = [
    [2, 2, 6],
    [3, 4, 9],
    [6, 8, 1]
]

resultado = suma_pares(matriz)
print("La suma de todos los numeros pares es:", resultado)
