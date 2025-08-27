# Exercício 6

""" Abaixo é apresentada a variável palavra. Com relação ao valor da variável palavra responda:

a) Quantas letras possui essa palavra?
b) Quantas vezes a letra 'o' aparece nessa palavra?
c) Qual a posição da letra v nessa palavra?
d) Escreva essa palavra de trás para frente.
e) Divida essa palavra em duas com a mesma quantidade de caracteres.
"""

palavra = "pneumoultramicroscopicossilicovulcanoconiotico"

# Item a) Tamanho da palavra (número de letras)
print("a) Quantidade de letras:", len(palavra))

# Item b) Quantidade de vezes que 'o' aparece
print("b) Quantas vezes aparece a letra 'o':", palavra.count("o"))

# Item c) Posição da letra 'v'
# .find retorna o índice (começa do 0). Se quiser posição "humana", soma +1.
posicao_v = palavra.find("v")
print("c) A posição da letra 'v' é:", posicao_v)


# Item d) Palavra de trás para frente (usando slicing [::-1])
print("d) Palavra invertida:", palavra[::-1])

# Item e) Dividir a palavra em duas metades iguais
metade = len(palavra) // 2
parte1 = palavra[:metade]
parte2 = palavra[metade:]
print("e) Duas metades da palavra:", parte1, "|", parte2)
