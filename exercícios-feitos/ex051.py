#Desafio 51 - Progressão Aritmética
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
print('Calculadora de Progressão aritmética!')
pri_ter = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
ult_ter = pri_ter + (razao * 10)
print('Os 10 primeiros termos da PA são: ')
for c in range (pri_ter, ult_ter, razao):
    print(c)
print('Fim da Execução')
