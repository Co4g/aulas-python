#Desafio 93 - Cadastro de Jogador de futebol
'''
Crie um programa que gerencia o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois, vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos 
durante o campeonato.
'''
#Declaração de variáveis
jog = dict()
gols = 0

#Corpo do programa
#inputs
jog['nome'] = str(input('Nome do jogador: '))
jog['partidas'] = int(input('Quantas partidas ele jogou? '))
for c in range(jog['partidas']):
    jog['gols'] = int(input(f'Quantos gols ele fez na {c+1}° partida? '))
    gols += jog['gols']
jog['gols'] = gols
#Exibição de Resultados:
print(f'O jogador {jog["nome"]} fez {jog["partidas"]} partidas ao longo do campeonato com um total de {jog["gols"]} gols!')