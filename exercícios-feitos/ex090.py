#Desafio 90 - Dicionário em Python
'''
Faça um programa que leia nome e média de um aluno, guardando a situação
(aprovado ou não) em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
#Declaração de variáveis
aluno = dict()

#Input de dados
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input('Digite a média do aluno: '))

#Corpo do programa
if aluno['média'] >= 6:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] = 'reprovado'

print(f'O aluno {aluno['nome']} ficou com média {aluno['média']} e sua situação é {aluno['Situação']}!')
