#Desafio 96 - Função que calcula área
'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''
def area(a, b):
    area = a * b
    print(f'A área do terreno é {area}m²!')

print('-='*15)
print('Calculador de Área'.center(30))
print('-='*15)

l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)