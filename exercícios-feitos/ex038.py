#Desafio 38 - Comparando números
'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
O primeiro valor é maior;
O segundo valor é maior
Não existe valor maior, os dois são iguais.
'''
print(50*'.')
print('        ESTE É UM COMPARADOR DE VALORES')
print(50*'.')
pri_val = int(input('Digite o primeiro valor para comparação: '))
seg_val = int(input('Digite o segundo valor para comparação: '))
if pri_val > seg_val:
    print(f'O primeiro valor, {pri_val}, é maior do que o segundo, {seg_val}!')
elif pri_val < seg_val:
    print(f'O segundo valor, {seg_val}, é maior do que o primeiro, {pri_val}!')
else:
    print(f'Os valores digitados são iguais!') 