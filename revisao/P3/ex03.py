# Dadas três listas fornecidas pelo usuário, transforme-as em conjuntos e mostre:
# - Elementos que aparecem em todas
# - Elementos que aparecem em exatamente duas
# - Elementos que aparecem em somente uma
# - Total de elementos distintos
A = [1, 2, 3, 4, 5]
B = [3, 4, 6, 7]
C = [4, 5, 8]

# - Elementos que aparecem em todas
comum = set(A) & set(B) & set(C)
print(comum)

# - Elementos que aparecem em exatamente duas


# - Elementos que aparecem em somente uma
unicos = set(A) ^ set(B) - set(C)
print(unicos)


print([0, 1, 2, 3, 4, 5][2:10])
