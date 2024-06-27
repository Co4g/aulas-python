#Funções para votação
'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, 
opcional ou obrigatório nas eleições. 
'''
#imports
from datetime import datetime

#definição de funções
def voto(ano_nas):
    ano_atual = datetime.now().year 
    idade = ano_atual - ano_nas
    if idade < 18:
        return 'não podem Votar!'
    elif idade > 18 and idade < 65:
        return 'têm voto obrigatório!'
    else:
        return 'têm voto opcional!'

#Corpo do Programa
nascimento = int(input('Digite o ano de seu nascimento: '))
pode_votar = voto(nascimento)
print(f'Pessoas nascidas em {nascimento} {pode_votar}')