#Desafio 35
'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo
'''
a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))
if a + b > c and a + c > b and b + c > a:
    print(f'Os valores {a}, {b} e {c} podem formar um triângulo!')
else:
    print(f'Os valores {a}, {b} e {c} não podem formar um triângulo!')