#Faça um programa que use a função valor_pagamento para determinar o valor a ser pago por uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valor_pagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.

def valor_pagamento(prestacao, dias_atraso):
    if dias_atraso == 0:
        return prestacao
    else:
        return prestacao + (prestacao * 0.03)

prestacao = float(input("Digite o valor da prestação: "))
dias_atraso = int(input("Digite o número de dias em atraso: "))
valor = valor_pagamento(prestacao, dias_atraso)
print("O valor a ser pago é: R$", valor)