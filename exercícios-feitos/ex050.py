#Desafio 50 - Soma dos Pares
'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
print('Somador de números pares!')
soma = 0
for c in range(0,6):
    usua = int(input('Digite um valor: '))
    par = usua % 2
    if par == 0:
        soma = soma + usua
print(f'A soma dos números pares digitados é: {soma}')
