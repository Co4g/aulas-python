#Desafio 95 - Aprimorando os dicionários
'''
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
#Declaração de variáveis
jog = dict()
gols = 0
total_jog = list()
#Corpo do programa
while True:
    #inputs
    jog['nome'] = str(input('Nome do jogador: '))
    jog['partidas'] = int(input('Quantas partidas ele jogou? '))
    for c in range(jog['partidas']):
        jog['gols'] = int(input(f'Quantos gols ele fez na {c+1}° partida? '))
        gols += jog['gols']
    jog['gols'] = gols
    total_jog.append(jog.copy())
    gols = 0
    continuar = str(input('Deseja continuar? [s/n]: '))
    if continuar in 'Nn':
        break
for i in total_jog:
    print(f'O jogador {i["nome"]} fez {i["partidas"]} partidas ao longo do campeonato com um total de {i["gols"]} gols!')
