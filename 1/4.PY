vector = [4, 2, 6, 8, 8, 1, 5, 7, 9, 9, 3, 0]

elemento_mayor = max(vector)
indices_elemento_mayor = [indice for indice, valor in enumerate(vector) if valor == elemento_mayor]

print(indices_elemento_mayor)
