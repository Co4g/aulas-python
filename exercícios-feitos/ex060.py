#Desafio 60 - Cálculo do Fatorial
'''
Faça um programa que leia um número qualquer e mostre seu fatorial.
'''
num = int(input('Digite um número para descobrir seu fatorial: '))
num2 = num
fatorado = num2 * (num2 -1)
num2 = num2 -2
if num == 0:
    print('O fatorial de 0 é igual a 1!')
else:
    while num2 > 0:
        fatorado = fatorado * num2
        num2 = num2 -1
    print(f'O fatorial de {num} é igual a {fatorado}!')