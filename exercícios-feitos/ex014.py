'''
Escreva um programa que converta uma temperatura digita em °C para °F
c = float(input('Digite a temperatura em °C:' ))
f = (c*1.8) + 32
k = c+273.15
print('A temperatura de {}°C é equivalente a {}°F e {}K!'.format(c, f, k))
'''
#Versão Nova
from time import sleep
print('°°'*20)
print('CONVERSOR DE TEMPERATURA'.center(40))
print('°°'*20)
sleep(0.3)
continuar = 's'
while continuar in 'Ss':
    while True:
        try:
            opção = int(input('''Olá, seja bem-vindo ao nosso conversor de temperatura!
                    1 - °C => °F
                    2 - °C => K
                    3 - °F => °C
                    4 - °F => K
                    5 - K => °C
                    6 - K => °F
                    Escolha que tipo de conversão deseja fazer: '''))
            break
        except ValueError:
            print('Digite um valor válido!')
    if opção == 1:
        while True:
            try:
                c = float(input('Digite a temperatura em °C: '))
                sleep(0.7)
                f = (c*1.8) + 32
                print(f'{c:.2f}°C = {f:.2f}°F')
                break
            except ValueError:
                print('Dado inválido, digite um número!')
    if opção == 2:
        while True:
            try:
                c = float(input('Digite a temperatura em °C: '))
                sleep(0.7)
                k = c + 273.15
                print(f'{c:.2f}°C = {k:.2f}K')
                break
            except ValueError:
                print('Dado inválido, digite um número!')
    if opção == 3:
        while True:
            try:
                f = float(input('Digite a temperatura em °F: '))
                sleep(0.7)
                c = (f-32) / 1.8
                print(f'{f:.2f}°F = {c:.2f}°C')
                break
            except ValueError:
                print('Dado inválido, digite um número!')
    if opção == 4:
        while True:
            try:
                f = float(input('Digite a temperatura em °F: '))
                sleep(0.7)
                k = (f + 459.67) * (5/9)
                print(f'{f:.2f}°F = {k:.2f}K')
                break
            except ValueError:
                print('Dado inválido, digite um número!')
    if opção == 5:
        while True:
            try:
                k = float(input('Digite a temperatura em K: '))
                sleep(0.7)
                c = k - 273.15
                print(f'{k:.2f}K = {c:.2f}°C')
                break
            except ValueError:
                print('Dado inválido, digite um número!')
    if opção == 6:
        while True:
            try:
                k = float(input('Digite a temperatura em K: '))
                sleep(0.7)
                f = (k - 273.15) * 1.8 + 32
                print(f'{k:.2f}K = {f:.2f}°F')
                break
            except ValueError:
                print('Dado inválido, digite um número!')
    print('=='*20)
    continuar = str(input('Deseja repetir o programa? [S/N]'))
sleep(0.5)
print('Programa encerrado, volte sempre!')
