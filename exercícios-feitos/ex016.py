'''
Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção inteira.
'''
import math
nr = float(input('Digite um número real: '))
ni = math.floor(nr)
print('A porção inteira do número real informado é {}!'.format(ni))