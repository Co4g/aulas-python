#Desafio 68 - Jogo do Par ou ímpar
'''
Faça um programa que jogue par ou ímpar com o computador. O jogo
só será interrompido quando o jogador perder. Mostrando o total
de vitórias consecutivas que ele conquistou ao final do jogo.
'''
from random import randint
c = 0
while True:
    num = randint(0, 1000)
    if num % 2 == 0:
        resultado = 1
    if num % 2 == 1:
        resultado = 2
    usuario = str(input('Você escolhe par ou ímpar [P|I]? '.lower()))
    if usuario in 'Pp':
        usu = 1
        computador = 2
    if usuario in 'Ii':
        usu = 2
        computador = 1
    if usu == resultado:
        print(f'Você venceu, o número era {num}!')
        c += 1
    if usu != resultado:
        print(f'Você perdeu, o número era {num}!')
        break
print(f'Você me venceu {c} vezes consecutivas!')
    

    

