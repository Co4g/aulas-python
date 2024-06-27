#Desafio 58 - Jogo da Adivinhação V2.0
'''
Melhore o desafio 28 onde o computador vai 'pensar' em um número de 0 até 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''
from random import randint
from time import sleep
print(35*'|')
print('BEM-VINDO AO JOGO DA ADIVINHAÇÃO!')
print(35*'|')
print('Funcionará da seguinte maneira: Eu pensarei em um número, e  você tentará adivinhar!\n'
    'Fique a vontade para tentar quantas vezes for necessário. Vamos lá, pensarei em um número de 0 a 10...')
computador = randint(0,10)
usuario = 11
sleep(1)
print('Já escolhi, agora tente adivinhar!')
c = 0
while usuario != computador:
    usuario = int(input('Qual número você acha que eu pensei? '))
    if usuario > 10 or usuario < 0:
        print('Não, você deve digitar um número entre 0 e 10!')
    if usuario != computador:
        print('Você errou, tente de novo...')
        c = c + 1
print(f'Parabéns, você acertou em {c} tentativas, eu tinha pensado no {computador}!')
