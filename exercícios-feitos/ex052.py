#Desafio 52 - Números Primos
'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
from math import isqrt
print('Descubra se o número é ou não primo!')
num = int(input('Digite um número inteiro para descobrirmos se é ou não primo: '))
raiz = isqrt(num)
if num <= 1:
    print(f'{num} não é um número primo!') 
elif num == 2:
    print(f'{num} é um número primo!')
elif num % 2 == 0:
    print('Não é primo!')
elif num > 3:
    for c in range (3, raiz + 1, 2):
        if num % c == 0:
            print('Não é primo!')
            break
    else:
        print('É primo!')

