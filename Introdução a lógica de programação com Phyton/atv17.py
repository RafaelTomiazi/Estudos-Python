# Exercício 1 - Verificação de Número
"""
Escreva um programa que receba um número do usuário e verifique se ele é positivo, negativo ou zero.
"""


num = float(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
    