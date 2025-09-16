# Você recebe uma string e sua tarefa é trocar casos. 
# Em outras palavras, converta todas as letras minúsculas
# em maiúsculas e vice-versa.
# Input: Fatec Rio Preto
# Output: fATEC rIO pRETO
string = input('Digite um texto: ')

resultado = ''
for letra in string:
    if letra.islower():
        resultado += letra.upper()
    else:
        resultado += letra.lower()

print(resultado)