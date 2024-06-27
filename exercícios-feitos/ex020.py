'''
Um professor quer sortear a ordem da apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do aluno quatro: ')
nomes = [a1, a2, a3, a4] 
ns = random.sample(nomes, k=4)
print('Alunos sorteados são, em ordem: 1° {}, 2° {}, 3° {} e 4° {}!'. format(ns[0], ns[1], ns[2], ns[3]))
