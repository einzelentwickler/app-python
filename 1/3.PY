import random

vector = [4, 2, 6, 8, 8, 1, 5, 7, 9, 9, 3, 0]

elemento_mayor = max(vector)
elementos_mayores = [indice for indice, valor in enumerate(vector) if valor == elemento_mayor]
elemento_seleccionado = random.choice(elementos_mayores)

print(elemento_mayor)
