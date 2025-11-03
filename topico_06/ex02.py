# Faça um programa que crie dois conjuntos x e y,
# com dez números inteiros cada um. Em seguida, crie:
# 1) Um conjunto resultante da união de x e y (todos os
# elementos de x e os elementos de y que não estão em x).
# 2) Um conjunto resultante da diferença entre x e y (todos
# os elementos de x que não existam em y).
# 3) Um conjunto resultante interseção entre x e y
x = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
y = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

union = x | y # x.union(y)
difference = x - y # x.difference(y)
intersection = x & y # x.intersection(y)

print(f'Union: {union} \nDifference: {difference} \nIntersection: {intersection}')