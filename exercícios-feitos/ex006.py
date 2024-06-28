#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada:
'''
#Versão 1.0
a = int(input('Digite um número: '))
print('O dobro de {} é: '.format(a), a*2)
print('O triplo de {} é: '.format(a), a*3)
print('A razia quadrada de {} é: '.format(a), a**2)
'''
#Versão revisada

from math import sqrt


while True:
    try:
        num = int(input('Digite um número int: '))
        break
    except ValueError:
        print('ERRO!!! digite um número inteiro válido!')

print(f'O dobro de {num} é {num*2}!')
print(f'O triplo de {num} é {num*3}!')
print(f'A raiz quadrada de {num} é {sqrt(num):.2f}!')