#Funções para sortear e somar
'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio()
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e 
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função
anterior.
'''
from random import randint
#definições de funções
def sorteio():
    for c in range(0,5):
        n = randint(0,10)
        números.append(n)
    print(f'Os números sorteados foram: {números}')
def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            listap.append(c)
            soma += c
    print(f'A soma dos números pares {listap} é: {soma}')
#Declaração de variáveis
números = list()
listap = list()
#Corpo do programa
sorteio()
somaPar(números)
