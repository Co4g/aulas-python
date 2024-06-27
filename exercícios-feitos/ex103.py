#Desafio 103 - Ficha do Jogador
'''
Faça um programa chamado ficha(), que receba dois parâmetros opcionais: o nome de um jogador 
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
que algum dado não tenha sido informado corretamente.
'''
#Imports

#Definição de funções
def ficha(nome='desconhecido', gols=None):
    print('-='*10)
    print('Ficha do jogador'.center(20))
    print('-='*10)
    print(f'Nome do jogador: {nome}')
    if gols == None:
        print('Quantidade de gols não informada')
    else:
        print(f'Gols feitos: {gols}')
#definição de variáveis
jogador = str(input('Informe o nome do jogador:  '.strip()))
gol = str(input(f'Informe a quantidade de gols de {jogador}: '.strip()))

#Corpo do Programa
if jogador in '' and gol in '':
    ficha()
elif gol in '':
    ficha(jogador)
elif jogador in '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)