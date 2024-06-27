#Desafio 67 - Tabuada v3.0
'''
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
from time import sleep
while True:
    num = int(input('Quer ver a tabuada de qual valor(digite número negativo para parar)? '))
    if num < 0:
        break
    print(f'A tabuada de {num} é:')
    print('¨'*30)
    for m in range(1, 11):
        tab = num * m
        print(num, 'x', m, '=', tab)
        sleep(0.2)
    print('¨'*30)
print('Programa encerrado!')
