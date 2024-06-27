#Função que descobre o maior
'''
Faça um programa que tenha uma função chamada maior(), que receberá vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from random import randint

#Definições das funções()
def maior(num):
    mai = max(num)
    print(f'O maior número da lista {lista} é: {mai}')
#Variáveis
lista = list()

#Corpo do programa
while True:
    números = randint(0,10)
    if números == 0:
        print('Número sorteado foi 0, portanto o maior número da lista é 0!')
    else:
        for c in range(números):
            n = randint(0,10)
            lista.append(n)
        maior(lista)
    cont = str(input('Deseja repetir? [S/N]: '))
    if cont not in 'Ss':
        print('Certo, programa encerrado!')
        break
    lista.clear()

'''
Neste código, notei que a ideia era criar minha própria função max(), porém eu simplesmente 
adicionei ela dentro da função contador e coloquei o print, deixando praticamente todo o
programa fora da função. Como o exercício era de função, considero que não tirei o proveito
que deveria ao escrever este código.
'''