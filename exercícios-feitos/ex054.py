#Desafio 54 - Grupo da Maioridade
'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
somama = 0 #Armazena a quantidade de pessoas maior de idade
somame = 0 #Armazena a quantidade de pessoas menor de idade
ano_atual = date.today().year #Armazena o ano atual, para descobrir a idade do usuário.
#Bloco para armazenamento de idade:
for c in range (0, 7): #Repetirá o loop 7 vezes, para armazenar sete usuários diferente.
    usuario = int(input('Digite seu ano de nascimento: '))
    maior = ano_atual - usuario #Calcula a idade do usuário.
    if maior >= 18:
        somama = somama + 1 #Se ele for maior de idade, adiciona 1 a variável somama
    else:
        somame = somame + 1 #Se ele for menor de idade, adiciona 1 a variável somame
#Bloco para informar a quantidade de usuários maiores de idade, respeitando o plural:
if somama == 1:
    print('Uma pessoa é maior de idade!')
elif somama > 1:
    print(f'{somama} pessoas são maiores de idade!')
else:
    print('Nenhum usuário é maior de idade!') 
#Bloco para informar a quantidade de usuários menores de idade, respeitando o plural:
if somame == 1:
    print('Uma pessoa é menor de idade!')
elif somame > 1:
    print(f'{somame} pessoas são menores de idade!')
else:
    print('Nenhuma pessoa é menor de idade!')




