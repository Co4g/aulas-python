#Desafio 84 - Lista composta e análise de dados
'''
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas fora cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves.
'''
#Declaração de variáveis
dados = list()
pessoas = list()
leves = list()
pesadas = list()

#Corpo do programa
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso em kg: ')))
    pessoas.append(dados[:])
    if dados[1] >= 100:
        pesadas.append(dados[:])
    elif dados[1] < 100:
        leves.append(dados[:])
    continuar = int(input('Deseja continuar? [1 - sim / 2 - não] '))
    dados.clear()
    if continuar != 1:
        break
print(f'As pessoas cadastradas foram {pessoas}!')
print(f'As pessoas mais pesadas(acima de 100kg) são: {pesadas}')
print(f'As pessoas mais leves(abaixo de 100kg) são: {leves})')



