#Desafio 46 - Contagem Regressiva
'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pause de 1 segundo entre eles.
'''
import time
from datetime import date
data_atual = date.today()
ano = data_atual.year
print('Olá, vamos fazer uma contagem para a estoura dos fogos para o Ano Novo?')
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
(print(f'Os fogos estouraram, feliz {ano}!'))
