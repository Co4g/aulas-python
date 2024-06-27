#Desafio 74 - Maior e menor valores em Tupla
'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
estão na tupla.
'''
#Este código contém a minha solução!
from random import randint
#Declaração de uma lista para armazenar os números:
lista_temporaria = [0, 1, 2, 3, 4]
index = 0
#Loop para preencher a lista
for c in range(0,5):
    #O randint gerará números que substituirão os cinco números originais na lista.
    lista_temporaria [index] = randint(0, 1000)
    index += 1
#Conversão da lista em uma tupla e posterior exibição do resultados!
nova_tupla = tuple(lista_temporaria)
print(f'A lista de números gerados foi: {nova_tupla}')
print(f'O maior valor da tupla é {max(nova_tupla)}')
print(f'O menor valor da tupla é: {min(nova_tupla)}')