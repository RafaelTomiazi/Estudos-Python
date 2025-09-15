# Exercício 8
"""
Escreva um programa que inicialize uma variável com o valor 5 para representar o número de milhas. 
Depois, converta esse valor para quilômetros e depois para metros, usando:
    km = milhas / 0.62137 
    metros = 1000 * km
Imprima o resultado na seguinte forma:

milhas
5
km
8.04674
metros
8046.74
"""
milhas = 5
km = milhas / 0.62137
metros = km * 1000
print("milhas")
print(milhas)
print("km")
print(round(km, 5))   
print("metros")
print(round(metros, 2))  # arredonda para 2 casas decimais
