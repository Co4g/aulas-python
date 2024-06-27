#Desafio 74 - Maior e menor valores em Tupla
'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
estão na tupla.
'''
#Este código contém a solução do Chat-GPT que me ensinou uma forma muito mais eficiente de adicionar elementos a tuplas:

from random import randint

# Gerar cinco números aleatórios e colocá-los em uma tupla
nova_tupla = tuple(randint(0, 1000) for _ in range(5)) #Ou repetir o randint(0,1000) cinco vezes divididos por vírgula.

# Exibir os resultados
print(f'A lista de números gerados foi: {nova_tupla}')
print(f'O maior valor da tupla é: {max(nova_tupla)}')
print(f'O menor valor da tupla é: {min(nova_tupla)}')

#Outra forma, que eu testei foi adicionar elementos à tupla da seguinte forma:
tupla = () #Tupla vazia
for _ in range(5):
    novo_elemento = randint(0, 1000)
    tupla = tupla + (novo_elemento,) #Adiciona o novo elemento gerado à tupla, que inicialmente estava vazia.
print(tupla)
