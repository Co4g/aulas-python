#Desafio 66 - Vários números com flag
'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles. 
'''
num = c = soma = 0
print('Iremos te pedir números infinitamente. Digite 999 para parar:')
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    c += 1
    soma += num
print(f'A quantidade de números digitados foi {c} e a soma total entre eles é {soma}!')


