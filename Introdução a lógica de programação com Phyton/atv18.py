# Exercício 2
"""
Escreva um código que peça ao usuário para inserir uma idade.
Verifique e exiba qual faixa etária ele pertence:
Infantil (0-12), Adolescente (13-17), Adulto (18-59) ou Idoso (60+).
"""


idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12:
    print("Faixa etária: Infantil")
elif 13 <= idade <= 17:
    print("Faixa etária: Adolescente")
elif 18 <= idade <= 59:
    print("Faixa etária: Adulto")
elif idade >= 60:
    print("Faixa etária: Idoso")
else:
    print("Idade inválida. Digite um número maior ou igual a 0.")
