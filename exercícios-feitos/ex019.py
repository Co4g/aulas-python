'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
escolhido.
'''
import random
nomes = ['Elwin', 'Arin', 'Kael', 'Felippo']
ae = random.choice(nomes)
print('O aluno que irá apagar o quadro será: ', ae)