'''
Um professor quer sortear a ordem da apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do aluno quatro: ')
nomes = [a1, a2, a3, a4] 
ns = random.sample(nomes, k=4)
print('Alunos sorteados são, em ordem: 1° {}, 2° {}, 3° {} e 4° {}!'. format(ns[0], ns[1], ns[2], ns[3]))
'''
import random
nomes = [] #define uma lista vazia, para ser preenchida com os inputs
aluno = 1 #Define o ordinal para o input. Função de estilo.
for c in range(4): #define um loop de 4 ciclos, para pedir o nome de 4 alunos.
    nome = input(f'Digite o nome do {aluno}° aluno: ')
    nomes.append(nome) #Adiciona o nome digitado no input anterior, a lista 'nomes'.
    aluno += 1

nomes_sorteados = random.sample(nomes, k=4) #ordena os nomes de forma aleatória em uma nova lista.
#Mostra de resultados
print(f'''Os alunos sorteados são, em ordem: 
      1° {nomes_sorteados[0]}
      2° {nomes_sorteados[1]}
      3° {nomes_sorteados[2]}
      4° {nomes_sorteados[3]}''')

