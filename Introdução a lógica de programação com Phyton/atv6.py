# Exercício 2
"""
Considere a variável mensagem do tipo str abaixo. Escreva um programa em Python que:

a) Imprima o primeiro caractere da string. 
b) Imprima o último caractere.
c) Imprima o último caractere de maneira diferente do item b.
d) Imprima o terceiro caractere da string.
e) Imprima os três primeiros caracteres da string.
f) Imprima os dois últimos caracteres da string.
g) Imprima o tamanho da string.

Dica: Lembre-se de que em Python, os índices das strings começam em 0.
"""

mensagem = "Instituto Infnet"


print("a) Primeiro caractere:", mensagem[0])
print("b) Último caractere:", mensagem[-1])
print("c) Último caractere (via len):", mensagem[len(mensagem) - 1])
print("d) Terceiro caractere:", mensagem[2])
print("e) Três primeiros caracteres:", mensagem[:3])
print("f) Dois últimos caracteres:", mensagem[-2:])

print("g) Tamanho da string:", len(mensagem))
