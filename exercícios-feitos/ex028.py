#Desafio 28
'''
 Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
print('Eu escolherei um número aleatório entre 0 e 5, tente descobrir qual...')
input('Aguarde um momento enquanto eu penso...')
num = [0, 1, 2, 3, 4, 5]
num_ran = random.choice(num)
num_usu = int(input('Já pensei! \nDigite o número que você acha que eu escolhi: '))
if num_ran == num_usu:
    print('Parabéns, você acertou!')
elif num_usu >5:
    print('Você é um idiota, eu mandei escolher entre 0 e 5 seu animal!')
else:
    print('Que pena, você errou!')
