#Desafio 88 - Palpites para a Mega Sena
'''
Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar 
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.
'''
from random import randint
from time import sleep
#Cabeçalho
print('°°°'*5, end='')
print('JOGO DA MEGA SENA', end='')
print('°°°'*5)
#Declaração de variáveis
qjogos = int(input('Quantos jogos serão gerados? '))
jogos = list() #Variável desnecessária...
palpite = list()
num = 6
n = 1
#Corpo do Programa
print('-=+'*25)
for c in range(qjogos):
    for q in range(num):
        valor = randint(1, 60)
        if valor not in palpite:
            palpite.append(valor)
        else:
            num += 1
    sleep(0.5)
    print(f'Jogo {n}: {palpite}')
    palpite.clear()
    n+=1
print('-=+'*25)