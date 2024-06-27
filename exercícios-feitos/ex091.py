#Desafio 91 - Jogos de dados em Python
'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número do dado.
'''
from random import randint
from time import sleep
#Declaração de variáveis
jogadores = dict()
resultados = list()
q = 1
vencedor = None
#Corpo do Programa
print('+++'*10)
print('JOGO DE DADOS'.center(30))
print('+++'*10)
for c in range(0,4):
    jogadores['nome'] = str(input(f'Digite o nome do {q}° jogador: '))
    jogadores['número'] = randint(1,6)
    print('Sorteando número...')
    sleep(1)
    q += 1
    print(f'O jogador {jogadores['nome']} recebeu o número {jogadores['número']}')
    resultados.append(jogadores.copy())

for jogador in resultados:
    if vencedor == None or jogador['número'] > vencedor:
        vencedor = jogador['número']
        nome_vencedor = jogador['nome']
print('calculando o vencedor...')
sleep(1)
print('A lista em ordem do maior para o menor ficou assim:')
lista_reordenada = sorted(resultados, key=lambda x: x['número'], reverse=True)
print(lista_reordenada)
print(f'O vencedor foi {nome_vencedor} com o número {vencedor}')