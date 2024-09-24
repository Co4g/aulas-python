"""
Faça um algoritmo que leia o salário do funcionário e mostre seu novo salário com 15% de aumento.
"""
nome = input('Olá, digite seu nome: ')
print(f'Olá, {nome}, bem-vindo ao novo sistema de informações de salário. Você receberá um aumento de 15%. Vamos descobrir quanto ficará seu salário!')
sal_atual = float(input('Digite seu atual salário: '))
valor_aumento = (sal_atual*15)/100
novo_sal = sal_atual + valor_aumento
print (f'{nome}, seu aumento será de R${valor_aumento:.2f}')
print(f'Seu novo salário, com aumento de 15% será de R${novo_sal:.2f}')