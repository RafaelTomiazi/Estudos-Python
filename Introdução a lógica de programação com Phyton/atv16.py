# Exercício 13
"""
Um número palíndromo é aquele que lido de trás pra frente é a mesma coisa que lendo de frente pra trás.
Exemplo: 121, 1991, 1001.

O programa deve:
- Ler um número do usuário
- Transformar em string para inverter
- Juntar o número original com o seu inverso
- Formar um palíndromo
"""


numero = input("Digite um número inteiro: ")
numero_invertido = numero[::-1]
palindromo = numero + numero_invertido


print("Número original:", numero)
print("Número invertido:", numero_invertido)
print("Número palíndromo:", palindromo)
