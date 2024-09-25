'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
escolhido.
'''
import random

nomes = ['Wesley', 'Thiago', 'Gabi', 'Matheus']
aluno_escolhido = random.choice(nomes)
print(f'O aluno que irá apagar o quadro será: {aluno_escolhido}')