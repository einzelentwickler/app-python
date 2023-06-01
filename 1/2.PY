import random

vector = [4, 2, 6, 8, 1, 5, 7, 9, 3, 0]

indices_pares = [indice for indice, _ in enumerate(vector) if indice % 2 == 0]
valores_pares = [vector[indice] for indice in indices_pares]

valores_aleatorios = random.sample(valores_pares, len(valores_pares))

for valor in valores_aleatorios:
    print(valor)
