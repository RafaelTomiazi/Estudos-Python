# Exercício 4
"""
Analise o seguinte programa abaixo. E faça o que é pedido nos itens:

a) Substitua os comentários em cima de cada linha por uma explicação do que aquela linha faz.
b) Note que a mensagem tem três problemas. O primeiro é que existe um hífen em 'A - Ginasta'. 
   O segundo é que a palavra ginasta aparece com letra maiuscula. 
   E por último, existem dois espaços entre em '... de Andrade  ganhou'. 
   Modifique os valores da variável nome e profissão para corrigir a mensagem.
"""

# Cria uma string com nome e profissão juntos
nome_e_profissao = "Rebeca Rodrigues de Andrade - Ginasta"

# Localiza a posição do caractere "-" dentro da string
posicao_hifen = nome_e_profissao.find("-")

# Separa o nome (da posição inicial até antes do hífen)
nome = nome_e_profissao[:posicao_hifen]

# Separa a profissão (do hífen até o final da string)
profissao = nome_e_profissao[posicao_hifen+1:]  # +1 para não incluir o hífen

# Remove espaços extras e coloca a profissão em minúsculo
nome = nome.strip()
profissao = profissao.strip().lower()

# Exibe a mensagem final corrigida
print("A", profissao, nome, "ganhou medalha de ouro no solo e prata no individual geral nas olimpíadas de Paris 2024.")
