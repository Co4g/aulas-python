#Desafio 92 - Cadastro de Trabalhador em Python
'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionário. Se por acaso o CTPS for diferente de zero, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, alem da idade, com quantos
anos a pessoa vai se aposentar.
'''
from datetime import date
from time import sleep

#Declaração de variáveis
trabalhador = dict()
data = date.today()
ano_atual = data.year
#Corpo do programa
print('°°°°'*10)
print('CADASTRO DA CARTEIRA DE TRABALHO'.center(40))
print('°°°°'*10)
#inputs
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Ano de nascimento'] = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = ano_atual - trabalhador['Ano de nascimento']
trabalhador['Carteira de trabalho'] = int(input('Número da Carteira de Trabalho(0 se não tiver): '))
if trabalhador['Carteira de trabalho'] != 0:
    trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: '))
    trabalhador['Idade de aposentadoria'] = (trabalhador['Ano de contratação'] - trabalhador['Ano de nascimento']) + 35

#Exibição de resultados
sleep(0.6)
print('Exibindo resultados...')
for k, v in trabalhador.items():
    print(k, '=', v)
    sleep(0.8)