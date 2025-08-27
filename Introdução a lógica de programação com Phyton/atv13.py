# Exercício 9

"""
Abaixo são apresentadas algumas frases da forma
    [sentenca0] se e somente se [sentenca1]

Para cada uma dessas frases transforme elas em variáveis booleanas no python e mostrar um exemplo 
em que a [sentenca1] é verdadeira e outra que ela é falsa.
"""

# Exemplo
print("Vou a praia se e somente se é fim de semana e meus amigos estão disponíveis")

# Verdadeira
e_fim_de_semana = True
amigos_disponiveis = True
vou_a_praia = e_fim_de_semana and amigos_disponiveis
print("vou_a_praia =", vou_a_praia)

# Falsa
e_fim_de_semana = True
amigos_disponiveis = False
vou_a_praia = e_fim_de_semana and amigos_disponiveis
print("vou_a_praia =", vou_a_praia)


# Item a
print("\nEu passo na prova se e somente se eu estudar e fizer os exercícios")

# Verdadeira
estudar = True
fazer_exercicios = True
passo_na_prova = estudar and fazer_exercicios
print("passo_na_prova =", passo_na_prova)

# Falsa
estudar = True
fazer_exercicios = False
passo_na_prova = estudar and fazer_exercicios
print("passo_na_prova =", passo_na_prova)


# Item b
print("\nEu posso ir distante se e somente se eu tenho um carro ou tenho uma bicicleta")

# Verdadeira
tenho_carro = False
tenho_bicicleta = True
posso_ir_distante = tenho_carro or tenho_bicicleta
print("posso_ir_distante =", posso_ir_distante)

# Falsa
tenho_carro = False
tenho_bicicleta = False
posso_ir_distante = tenho_carro or tenho_bicicleta
print("posso_ir_distante =", posso_ir_distante)


# Item c
print("\nEu vou dormir se e somente se estou cansado ou é tarde")

# Verdadeira
estou_cansado = False
e_tarde = True
vou_dormir = estou_cansado or e_tarde
print("vou_dormir =", vou_dormir)

# Falsa
estou_cansado = False
e_tarde = False
vou_dormir = estou_cansado or e_tarde
print("vou_dormir =", vou_dormir)


# Item d
print("\nEu vou viajar se e somente se eu tenho dinheiro e tempo")

# Verdadeira
tenho_dinheiro = True
tenho_tempo = True
vou_viajar = tenho_dinheiro and tenho_tempo
print("vou_viajar =", vou_viajar)

# Falsa
tenho_dinheiro = True
tenho_tempo = False
vou_viajar = tenho_dinheiro and tenho_tempo
print("vou_viajar =", vou_viajar)
