#Desafio 30
'''
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
'''
num = int(input('Digite um número: '))
par_impar = num % 2
if par_impar == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é impar')