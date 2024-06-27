'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
import math
co = float(input('Digite o valor do Cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = math.sqrt(math.pow(co, 2)+math.pow(ca, 2))
print('A hipotenusa possui o valor de {:.2f}cm!'.format(hp))
