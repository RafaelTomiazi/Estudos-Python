#Construa um programa que contenha uma função chamada soma_imposto. A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobrevendas expressa em porcentagem e o custo, que é o custo de um produto antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(taxa_imposto, custo):
    imposto = (taxa_imposto / 100) * custo
    return imposto
taxa_imposto = float(input("Digite a taxa de imposto: "))
custo = float(input("Digite o custo do produto: "))
imposto = soma_imposto(taxa_imposto, custo)
print("O imposto sobre vendas foi de: R$", imposto)
