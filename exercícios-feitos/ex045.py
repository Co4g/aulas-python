#Desafio 45 - Pedra, Papel e Tesoura.
'''
Crie um programa que faça o computador jogar Jokenpô com você
'''
from random import randint
import time
print('Olá, vamos jogar Jokenpô?\nEu começarei escolhendo e você escolherá depois!')
time.sleep(1)
list = [0, 1, 2]
comp = randint(0, 2)
print('Pronto, já escolhi, agora é sua vez!')
usuario = str(input('Escolha entre Pedra, Papel e Tesoura:\n'
                    '1 - Pedra\n'
                    '2 - Papel\n'
                    '3 - Tesoura\n'))
if usuario == '1':
    if comp == 0:
        print('Eu escolhi pedra também, é um empate!')
    elif comp == 1:
        print('Eu escolhi papel, você perdeu!')
    elif comp == 2:
        print('Eu escolhi tesoura, parabéns, você venceu!')
elif usuario == '2':
    if comp == 0:
        print('Eu escolhi pedra, você venceu. Parabéns!')
    elif comp == 1:
        print('Eu também escolhi papel, é um empate!')
    elif comp == 2:
        print('Eu escolhi tesoura, você perdeu!')
elif usuario == '3':
    if comp == 0:
        print('Eu escolhi pedra, você perdeu!!')
    elif comp == 1:
        print('Eu escolhi papel, incrível, vocÊ ganhou!')
    elif comp == 2:
        print('Eu escolhi tesoura, é um empate!')
else:
    print('Deixe de ser burro, é pra escolher entre 1, 2 ou 3!')
    exit()
    