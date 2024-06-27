#Desafio 63 - Sequência de Fibonacci v1.0
'''
escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros termos de uma sequência de fibonacci.
'''
n = int(input('Quantos termos da sequência de Fibonacci vocÊ gostaria de ver? '))
a = 0
b = 1
c = 0
f = 1
if n == 1:
    print('0')
elif n > 1:
    print('0')
    while c < n:
        print(f, end = '|')
        b = f
        f = a + b
        a = b
        c += 1
else:
    print('Certo, não mostraremos nenhum termo!')
