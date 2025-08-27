# Exercício 3
"""
Escreva um programa que pede para o usuário entrar uma certa quantidade de minutos. 
O programa deve fazer a conversão dessa quantidade em minutos para o formato hora:minuto. 
Por exemplo, caso o usuário passe o valor de 80 o programa deve mostrar para o usuário que isso 
é equivalente a 1:20. O seu código deve conter comentários para explicar o que está fazendo 
nas principais linhas
"""

minutos = int(input("Digite a quantidade de minutos: "))
horas = minutos // 60
resto_minutos = minutos % 60

print("então as horas corretas são:",horas,":",resto_minutos)