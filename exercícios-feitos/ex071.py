#Desafio 71 - Simulador de Caixa Eletrônico
'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(int)
e o programa vai informar quantas cédulas de cada valor serão entregues.
obs: Considerar que o caixa possuí cédulas de R$50, R$20, R$10 e R$1.
'''


#Corpo do Programa
while True:
    nota_50 = 0
    nota_20 = 0
    nota_10 = 0
    nota_1 = 0
    valor_inicial = int(input('Quanto você quer sacar?'))
    valor = valor_inicial
    if valor >= 50:
        nota_50 = valor // 50
    valor = valor - (nota_50*50)
    if valor >= 20:
        nota_20 = valor // 20
    valor = valor - (nota_20*20)
    if valor >= 10:
        nota_10 = valor // 10
    valor = valor - (nota_10*10)
    if valor >= 1:
        nota_1 = valor // 1
    valor = valor - (nota_1*1)
    print(f'O valor sacado é {valor_inicial} e foram retiradas {nota_50} notas de R$50, {nota_20} de R$20, {nota_10} de R$10 e {nota_1} de R$1.')
    continuar = str(input('Deseja fazer outro saque? [s/n]'))
    if continuar.lower() != 's':
        break 
print('Programa encerrado, volte sempre!')