# Exercício 11
"""
Dado o texto na variável mensagem, faça um programa que conta a porcentagem de vogais 
em relação a todos os caracteres da string (espaços e pontuações devem ser contabilizados). 
Seu programa deve ter comentários. (Cuidado com as vogais maiúsculas)
"""

mensagem = """A importancia da persistencia no aprendizado de programacao nao pode ser subestimada. 
Assim como em qualquer outra habilidade, a pratica constante e a dedicacao sao fundamentais para alcançar a proficiencia. 
Inicialmente, a complexidade de certas linguagens e conceitos pode parecer desafiadora, 
mas com o tempo e a experiencia, o aprendizado se torna mais intuitivo e gratificante."""


vogais = "aeiouAEIOU" #todas as vogais
total_caracteres = len(mensagem) # Conta o total de caracteres na mensagem ncluindo letras, espaços e pontuações
total_vogais = sum(1 for char in mensagem if char in vogais)# Conta quantas vogais existem no texto

porcentagem_vogais = (total_vogais / total_caracteres) * 100 #porcentagem de vogais


print("Total de caracteres:", total_caracteres)
print("Total de vogais:", total_vogais)
print("Porcentagem de vogais: {:.2f}%".format(porcentagem_vogais))
