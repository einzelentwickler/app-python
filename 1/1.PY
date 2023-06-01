import random

# Crear un vector vacío
vector = []

# Generar los valores aleatorios y agregarlos al vector
for _ in range(100):
    numero = random.randint(0, 10)
    vector.append(numero)

# Imprimir el vector
print(vector)
