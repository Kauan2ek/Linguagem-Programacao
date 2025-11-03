# Dadas três listas de números inteiros,
# imprima os elementos comuns entre elas.
x = [1, 2, 3]
y = [3, 4, 5]
z = [2, 3, 4]

x = set(x)
y = set(y)
z = set(z)

print(x & y & z)
