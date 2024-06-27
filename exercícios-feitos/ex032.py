#Desafio 32
'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto
'''
ano = int(input('Escreve o ano que deseja saber se é ou não bissexto: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é bissexto!')
        else:
            print(f'O ano {ano} não é bissexto!')
    else:
        print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!') 

