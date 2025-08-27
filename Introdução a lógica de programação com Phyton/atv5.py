# Exercício 1
# Considere as seguintes atribuições nas variáveis abaixo e responda as perguntas:
# a0 = 10
# a1 = "10"
# a2 = 10.0
#
# Perguntas:
# 1. Qual o tipo das variáveis a0, a1 e a2?
# 2. Qual o tipo das variáveis b0, b1, b2, b3 e b4?
# 3. Qual o tipo das variáveis isso_eh_um_int, isso_eh_um_float e isso_eh_uma_string?
# 4. Qual seria o tipo da variável entrada_do_usuario = input()?

a0 = 10
a1 = "10"
a2 = 10.0

b0 = a0 + a2
b1 = a2 + a2
b2 = 5 * a0
b3 = a0 // 2
b4 = a0 / 2

isso_eh_um_int = 10.0
isso_eh_um_float = "10"
isso_eh_uma_string = 10

# Respostas usando type()
print("a0:", type(a0))  
print("a1:", type(a1))   
print("a2:", type(a2))   

print("b0:", type(b0))   
print("b1:", type(b1))  
print("b2:", type(b2))   
print("b3:", type(b3))   
print("b4:", type(b4))   

print("isso_eh_um_int:", type(isso_eh_um_int))         # float
print("isso_eh_um_float:", type(isso_eh_um_float))     # str
print("isso_eh_uma_string:", type(isso_eh_uma_string))  # int

# Entrada do usuário com input sempre gera str
# Se quiser inteiro: entrada = int(input("Digite um número: "))
