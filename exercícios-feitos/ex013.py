"""
Faça um algoritmo que leia o salário do funcionário e mostre seu novo salário com 15% de aumento.
"""

a = float(input('Digite seu atual salário: '))
va = (a*15)/100
ns = a + va
print ('Seu aumento será de:', va, 'reais')
print('Seu novo salário, com aumento de 15% será:', ns, 'reais')